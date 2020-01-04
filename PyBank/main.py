
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
# Lists
with open("budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    pybank_header = next(pybank_reader)

    month_list = []
    for row in pybank_reader:
        month_list.append(row[0])
    #print(month_list)

with open("budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')
    pybank_header = next(pybank_reader)

    profit_list = []
    for row in pybank_reader:
        profit_list.append(row[1])  
    #print(profit_list)
    
    changes = [int(profit_list[i + 1]) - int(profit_list[i]) for i in range(len(profit_list)-1)]
    #changes = [j - i for i, j in zip(profit_list[: -1], profit_list[1 :])]
    #print(str(changes))
    
    average = round(sum(changes) / len(changes),2)
    print(f"Average Change: ${average}")

# The greatest increase in profits (date and amount) over the entire period
    increase = max(changes)
    max_changes_index = (changes.index(increase)+1)
    print(f"Greatest Increase in Profits: {month_list[max_changes_index]}  (${increase})")

# The greatest decrease in losses (date and amount) over the entire     
    decrease = min(changes)
    min_changes_index = (changes.index(increase)+1)
    print(f"Greatest Decrease in Profits: {month_list[min_changes_index]}  (${decrease})")
    
# Output

f = open("results.txt","w+")

f.write("Financial Analysis\n")
f.write("-------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${net_total}\n")
f.write(f"Average Change: ${average}\n")
f.write(f"Greatest Increase in Profits: {month_list[max_changes_index]}  (${increase})\n")
f.write(f"Greatest Decrease in Profits: {month_list[min_changes_index]}  (${decrease})\n")

f.close()
    



