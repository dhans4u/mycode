## this works when your CSV data has headers

import csv

with open('mycsv.csv', 'r') as csv_file:
    csv_dict = csv.DictReader(csv_file)
    for row in csv_dict:
        print(row["ip"])
