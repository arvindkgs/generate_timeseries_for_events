from datetime import timedelta
from lib.TimeUnit import TimeUnit
import bisect


def roundSecondsFloor(timestamp):
    if timestamp.second > 0 or timestamp.microsecond > 0:
        return timestamp.replace(second=0, microsecond=0)
    else:
        return timestamp


def roundSecondsCeiling(timestamp):
    if timestamp.second > 0 or timestamp.microsecond > 0:
        minutes_ = timestamp + timedelta(minutes=1)
        return minutes_.replace(second=0, microsecond=0)
    else:
        return timestamp

def computeTimeSeries(timeFrame, events):

    events.sort(key=lambda event: event.timestamp)

    epochTS = events[0].timestamp
    timeFrameEndTS = roundSecondsCeiling(epochTS + timedelta(minutes=timeFrame))
    timeUnits = []
    for i, currEvent in enumerate(events):
        if currEvent.timestamp < timeFrameEndTS:
            endCurrEventTS = currEvent.timestamp + timedelta(minutes=currEvent.duration)
            currEventTS = roundSecondsFloor(currEvent.timestamp)
            while currEventTS <= timeFrameEndTS and endCurrEventTS > currEventTS:
                lowertimeunit = currEventTS - timedelta(minutes=1)
                unit = TimeUnit(lowertimeunit, currEventTS)
                if currEvent.timestamp <= currEventTS:
                    if unit not in timeUnits:
                        bisect.insort_left(timeUnits, unit)
                    timeUnits[timeUnits.index(unit)].addEvent(currEvent)
                else:
                    if unit not in timeUnits:
                        bisect.insort_left(timeUnits, unit)
                currEventTS = currEventTS + timedelta(minutes=1)
            #Add entries when current Event completes before the next event
            if i < len(events) - 1:
                nextEvent = roundSecondsFloor(events[i+1].timestamp)
                while currEventTS < nextEvent:
                    lowertimeunit = currEventTS - timedelta(minutes=1)
                    bisect.insort_left(timeUnits, TimeUnit(lowertimeunit, currEventTS))
                    currEventTS = currEventTS + timedelta(minutes=1)
    # Add entries for when time frame is still pending after completion of events
    while currEventTS < timeFrameEndTS:
        lowertimeunit = currEventTS - timedelta(minutes=1)
        bisect.insort_left(timeUnits, TimeUnit(lowertimeunit, currEventTS))
        currEventTS = currEventTS + timedelta(minutes=1)

    return timeUnits
