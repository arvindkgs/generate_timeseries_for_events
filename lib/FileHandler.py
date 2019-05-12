import json
from Event import Event

'''
Helper methods to read events file and write output file 
'''


def read(eventsFile):
    eventsStr = '[' + eventsFile.read() + ']'
    eventsStr = eventsStr.replace('\n', ',')
    eventsDict = json.loads(eventsStr)
    events = []
    for eventItem in eventsDict:
        events.append(Event(**eventItem))
    return events


def write(outputFile, items):
    with open(outputFile, 'w') as toFile:
        for item in items:
            toFile.write(str(item) + "\n")
    pass
