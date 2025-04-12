import pickle

from pathlib import Path
from athletelist import AthletList



file_dir = Path.cwd() / 'data' / 'athletes.pickle'

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthletList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print(f'File error {ioerr}')
        return None

def put_to_store(files):
    athletes = {}
    for file in files:
        athlete = get_coach_data(file)
        athletes[athlete.name] = athlete
    try:
        with open(file_dir, 'wb') as athf:
            pickle.dump(athletes, athf)
    except IOError as ioerr:
        print(f'File error (put_to_store) {ioerr}')
    return athletes

def get_from_store():
    athletes = {}
    try:
        with open(file_dir, 'rb') as athf:
            athletes = pickle.load(athf)
    except IOError as ioerr:
        print(f'File error (get_from_store): {ioerr}')
    return athletes
