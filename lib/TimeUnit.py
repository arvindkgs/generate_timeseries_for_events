'''
Time Unit represents statistics in a time slot
'''


class TimeUnit(object):
    def __init__(self, fromTS, toTS, average_delivery_time=0, duration=1, **kwargs):
        self.fromTS = fromTS
        self.toTS = toTS
        self.average_delivery_time = average_delivery_time
        self.duration = duration
        self.words = 0
        self.events = []
        for key, value in kwargs:
            if key == 'words':
                self.words = int(value)

    def addEvent(self, event, noOfWords):
        self.average_delivery_time = float(self.average_delivery_time * len(self.events) + event.duration) / (
                len(self.events) + 1)
        self.events.append(event)
        self.words += noOfWords

    def __str__(self):
        return '{ "date": "' + str(self.toTS) + '", "average_delivery_time": ' + str(
            self.average_delivery_time) + ', "words":' + str(int(self.words)) + ' }'

    def __eq__(self, other):
        return isinstance(other, TimeUnit) and other.fromTS == self.fromTS and other.toTS == self.toTS

    def __lt__(self, other):
        return self.toTS < other.toTS and self.fromTS < other.fromTS
