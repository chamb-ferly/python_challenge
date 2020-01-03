
#PyBank

import csv



#The total number of months included in the dataset
total_months = 0
with open("budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    next(pybank_reader)

    for row in pybank_reader:
        total_months += 1

print(f"Total Months: {total_months}")

# The net total amount of "Profit/Losses" over the entire period
net_total = 0
with open("budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    next(pybank_reader)

    for row in pybank_reader:
            net_total += int(row[1])

print(f"Total: ${net_total}")

# The average of the changes in "Profit/Losses" over the entire period
with open("budget_data.csv", 'r') as csvfile, open("delta.csv", 'w+') as csvoutput:
    pybank_dict = csv.DictReader(csvfile)
    fieldnames = pybank_dict.fieldnames + ['Change']
    change_dict = csv.DictWriter(csvoutput, fieldnames)
    change_dict.writeheader()
    for change, row in enumerate(pybank_dict, 0):
        change_dict.writerow(dict(row, Change='delta here'))

with open("delta.csv") as csvfile: 
    delta_dict = csv.DictReader(csvfile, 'r')   
    for line in delta_dict:
        print(line)
        #delta = row['Profit/Losses']
        #pybank_dict.update({'Change': delta})  



# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire 