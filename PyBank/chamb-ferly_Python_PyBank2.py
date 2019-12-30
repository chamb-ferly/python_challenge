
import csv

with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyBank\main.py\budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    print(pybank_reader)

    pybank_header = next(pybank_reader)
    print(f"File Header: {pybank_header}")

    for row in pybank_reader:
        print(row)


#The total number of months included in the dataset
total_months = 0
with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyBank\main.py\budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(pybank_reader)
    for row in pybank_reader:
        total_months += 1

print(f"Total Months: {total_months}")

# The net total amount of "Profit/Losses" over the entire period
net_profit = 0
profit_loss_index = 1

with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyBank\main.py\budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(pybank_reader)
    for row in pybank_reader:
        float_net = float(row[profit_loss_index])
        net_profit += float_net

print(f"Total: ${net_profit}")

# The average of the changes in "Profit/Losses" over the entire period
  
# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period