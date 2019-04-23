#!/usr/bin/python3
"""Learning to parse out JSON | rzfeeser@alta3.com"""
from pprint import pprint
import json

with open("/home/student/fry.facts", "r") as fry:
    fryson = json.loads(fry.read())
 
print(fryson)
pprint.pprint(fryson)
