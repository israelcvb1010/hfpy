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
    

def get_coach_data(filename):
    filepath = f'../data/{filename}'
    try:
        with open(filepath) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthletList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print(f'File error {ioerr}')
        return None


james = get_coach_data('james.txt')
print(james.top3())

julie = get_coach_data('julie.txt')
print(julie.top3())