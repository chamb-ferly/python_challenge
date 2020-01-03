#PyBank

import csv

with open("budget_data.csv") as f:
    pybank_reader = csv.DictReader(f, delimiter=',')
    print(pybank_reader)

#The total number of months included in the dataset
total_months = 0
with open("budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')

    for row in pybank_reader:
        total_months += 1

print(f"Total Months: {total_months -1}")

    

    if csv.Sniffer().has_header:
        next(pypoll_reader)
    for row in pypoll_reader:
        if row[2] not in Candidates:

            vote_percent = round(((vote_count / total_votes) * 100) ,3)
print(vote_percent)


pypoll_dict = csv.DictReader(open("election_data.csv", 'r'))
mydict = []
for line in pypoll_dict:
    mydict.append(line)

import collections
vote_count = collections.Counter(e['Candidate'] for e in mydict)



with open("election_data.csv", 'r') as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')
    next(pypoll_reader)

    for row in pypoll_reader:
        if row[2] == 'Khan':
            KhanCount = KhanCount + 1
        elif row[2] == 'Correy':
            CorreyCount = CorreyCount + 1
        elif row[2] == "O'Tooley":
            TooleyCount = TooleyCount + 1
        elif row[2] == 'Li':
            LiCount = LiCount + 1

print(KhanCount)


reader = csv.reader(open('budget_data.csv', 'rb'))
writer = csv.writer(open('output.csv', 'w+'))
headers = reader.next()
headers.append("Delta")
writer.write(headers)
for row in reader:
    row.append()


    with open("budget_data.csv", "r") as csvfile:
    pybank_reader = csv.reader(csvfile)
    pybank_reader = list(pybank_reader)
    i = 1
    j = 2
    for row in pybank_reader[1]:
        print(f"{row + str(1)} - {row}")

           count = 0
    for row in pybank_reader:  
        if count != 0: # if this isn't the first time in the loop (ie. if you have a number to subtract)  
            count = count + 1  
            row.blankcolumnname = row[Profit/Losses] - previous # make the blank column = current - previous  
            pybank_reader.updateRow(row) # updates the whole row, now with a value for the blank column  
            previous = row[1] # sticks the current value into the previous variable for the next time through the loop  
        else: # do this if it is the first time in the loop  
            count = 1  
            previous = row[1]


            
    i = 1
    j = 2

    for row in pybank_list:
        print(int(row[i] - int(row[j])))


          if value != 0:
            delta += (int(row[i]) - int(row[i-1]))
            pybank_dict.update(delta)
        elif value == 0:
            print(f'{delta_dict["delta"]})


              j += int(row[i])
        k += int(row[i - 1]) 
        row.update('Change')
        pybank_dict.append({'Change':j-k})
    print(pybank_dict)


        pybank_dict = csv.DictReader(csvfile, delimiter=',')
    i = 2    
    for row in pybank_dict:
        print(row['Date'], row['Profit/Losses'])
        delta = row['Profit/Losses']
        pybank_dict.update({'Change': delta})  

        fields = []
rows = []
with open("budget_data.csv") as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=',')

fields = pybank_reader.next()
for row in pybank_reader:
    rows.append(row)