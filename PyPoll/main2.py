#PyBank

import csv

with open("budget_data.csv") as csvfile:
    pybank_reader = csv.DictReader(csvfile, delimiter=',')
    print(pybank_reader)

    pybank_header = next(pybank_reader)
    print(pybank_header)
    

