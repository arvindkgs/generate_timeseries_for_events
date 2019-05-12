from datetime import timedelta
from lib.TimeUnit import TimeUnit
import bisect

'''
This file contains methods to compute time series in chronological order for given set of discrete events
'''

# Retuns timestamp rounded to closest minute in the lower bound
def roundSecondsFloor(timestamp):
    if timestamp.second > 0 or timestamp.microsecond > 0:
        return timestamp.replace(second=0, microsecond=0)
    else:
        return timestamp


# Retuns timestamp rounded to closet minute in the upper bound
def roundSecondsCeiling(timestamp):
    if timestamp.second > 0 or timestamp.microsecond > 0:
        minutes_ = timestamp + timedelta(minutes=1)
        return minutes_.replace(second=0, microsecond=0)
    else:
        return timestamp


# Returns timeunits for given timeFrame, events, and timeSlot in minutes
def computeTimeSeries(timeFrame, events, timeSlotMinutes):
    events.sort(key=lambda event: event.timestamp)

    epochTS = events[0].timestamp
    timeFrameEndTS = roundSecondsCeiling(epochTS + timedelta(minutes=timeFrame))
    timeUnits = []
    for i, currEvent in enumerate(events):
        if currEvent.timestamp < timeFrameEndTS:
            endCurrEventTS = currEvent.timestamp + timedelta(minutes=currEvent.duration)
            currEventTS = roundSecondsFloor(currEvent.timestamp)
            currWords = 0.0
            while currEventTS <= timeFrameEndTS and endCurrEventTS > currEventTS:
                lowertimeunit = currEventTS - timedelta(minutes=timeSlotMinutes)
                unit = TimeUnit(lowertimeunit, currEventTS)
                if currEvent.timestamp <= currEventTS:
                    if unit not in timeUnits:
                        bisect.insort_left(timeUnits, unit)
                    currWords += currEvent.wordsPerMinute * timeSlotMinutes
                    noOfWords = 0
                    if currWords != 0:
                        noOfWords = int(currEvent.wordsPerMinute * timeSlotMinutes)
                        if currWords.is_integer() and not currEvent.wordsPerMinute.is_integer():
                            noOfWords += 1
                    timeUnits[timeUnits.index(unit)].addEvent(currEvent, noOfWords)
                else:
                    if unit not in timeUnits:
                        bisect.insort_left(timeUnits, unit)
                currEventTS = currEventTS + timedelta(minutes=timeSlotMinutes)
            # Add entries when current Event completes before the next event
            if i < len(events) - 1:
                nextEvent = roundSecondsFloor(events[i + 1].timestamp)
                while currEventTS < nextEvent:
                    lowertimeunit = currEventTS - timedelta(minutes=timeSlotMinutes)
                    bisect.insort_left(timeUnits, TimeUnit(lowertimeunit, currEventTS))
                    currEventTS = currEventTS + timedelta(minutes=timeSlotMinutes)

    # Add entries for when time frame is still pending after completion of events
    while currEventTS < timeFrameEndTS:
        lowertimeunit = currEventTS - timedelta(minutes=timeSlotMinutes)
        bisect.insort_left(timeUnits, TimeUnit(lowertimeunit, currEventTS))
        currEventTS = currEventTS + timedelta(minutes=timeSlotMinutes)

    return timeUnits
