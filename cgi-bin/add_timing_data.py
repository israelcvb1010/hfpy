#!/usr/bin/env python3

import cgi
import os
import time
import sys
import yate


# Query three environment variables ans assign their values to variables
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']

# Get the current time
cur_time = time.asctime(time.localtime())

# Display the queried data on standard error
print(yate.start_response())
print(yate.start_page("Add new timing data"))

print(yate.include_footer({"Home": "/index.html", "Select another athlete:": "generate_list.py"}))
