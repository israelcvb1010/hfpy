class AthletList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def sanitize(self, time):
        if '-' in time:
            splitter = '-'
        elif '.' in time:
            splitter = '.'
        else:
            return time
        mins, secs = time.split(splitter)
        return f'{mins}:{secs}'

    def top3(self):
        return sorted(set([self.sanitize(time) for time in self]))[0:3]
    
