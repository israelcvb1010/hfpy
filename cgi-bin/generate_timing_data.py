#!/usr/bin/env python3

import cgi
import athletemodel
import yate


athletes = athletemodel.get_from_store()

# Grab all of the form data and put it in a directory
form_data = cgi.FieldStorage()
athlete_name = form_data['athlete'].value

print(yate.start_response())
print(yate.start_page("Generate time data"))
print(yate.header(f"Athlete: {athlete_name}, DOB: {athletes[athlete_name].dob}."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html", "Select another athlete:": "generate_list.py"}))