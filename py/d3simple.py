#!/usr/bin/python3

import datetime

now = str(datetime.date.today())
print(now)

with open("ansible-"+now+".file", "a") as transunion:
    transunion.write("I made this :)\n")
