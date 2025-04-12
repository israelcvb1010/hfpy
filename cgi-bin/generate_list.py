#!/usr/bin/env python3

import glob
import athletemodel
import yate


files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(files)

print(yate.start_response())
print(yate.start_page('Coach'))
print(yate.include_header("Coach Kelly's List Of Athletes"))
print(yate.start_form('generate_timing_data.py'))

# Generate a radio-button for each of your athlete
print(yate.para("Select an athlete from the list to work with:"))
for athlete in athletes:
    print(yate.radio_button("athlete", athletes[athlete].name))

# End the form
print(yate.end_form())

# End the page
print(yate.include_footer({'Home': '/index.html'}))
