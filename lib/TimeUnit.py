'''
Time Unit represents statistics in a timeslot
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

    def addEvent(self, event):
        self.average_delivery_time = float(self.average_delivery_time * len(self.events) + event.duration) / (len(self.events)+1)
        self.events.append(event)

    def __str__(self):
        return '{ "date": "' + str(self.toTS) + '", "average_delivery_time": ' + str(self.average_delivery_time) +' }'

    def __eq__(self, other):
        return isinstance(other, TimeUnit) and other.fromTS == self.fromTS and other.toTS == self.toTS

    def __lt__(self, other):
        cmp = self.toTS < other.toTS and self.fromTS < other.fromTS
        #print str(cmp)+" - self.toTS("+str(self.toTS)+") < other.fromTS("+str(other.fromTS)+")"
        return cmp
