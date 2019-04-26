#!/usr/bin/python3

import urllib.request
import json


def main():
    ourresponse = urllib.request.urlopen('http://api.open-notify.org/astros.json')

    stringdata = ourresponse.read().decode('utf-8')

    dictdata = json.loads(stringdata)

    for record in dictdata.get('people'):
        print(record['name'])


main()
