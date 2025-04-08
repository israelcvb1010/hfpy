#!/usr/bin/env python3

import glob
import athletemodel
import yate


files = glob.glob('../data/*.txt')
athletes = athletemodel.put_to_store(files)

print(yate.start_response())
print(yate.include_header("Coach Kelly's List Of Athletes"))
