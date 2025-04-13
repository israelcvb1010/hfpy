#! /usr/bin/env python3

import yate


print(yate.start_response())
print(yate.do_form('add_timing_data.py', ['TimeValue'], text='Send'))