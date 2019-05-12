from datetime import datetime

class Event:
    def __init__(self, **kwargs):
        if 'timestamp' not in kwargs:
            raise TypeError('timestamp is required for event')
        if 'duration' not in kwargs:
            raise TypeError('duration is required for event')
        self.nr_words = 0
        for (key, value) in kwargs.iteritems():
            if key == 'timestamp':
                self.timestamp = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
            if key == 'duration':
                self.duration = int(value)
            if key == 'nr_words':
                self.nr_words = int(value)
            elif key == 'translation_id':
                self.translationid = value
            elif key == 'source_language':
                self.source_language = value
            elif key == 'target_language':
                self.target_language = value
            elif key == 'client_name':
                self.client_name = value
            elif key == 'event_name':
                self.event_name = value

    def __str__(self):
        return str(vars(self))