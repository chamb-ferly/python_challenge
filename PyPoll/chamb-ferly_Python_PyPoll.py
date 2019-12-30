import csv

with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyPoll\main.py\election_data.csv") as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')
    print(pypoll_reader)

    pypoll_header = next(pypoll_reader)
    print(pypoll_header)
    
# The total number of votes cast
total_votes = 0
with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyPoll\main.py\election_data.csv") as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')

    for row in pypoll_reader:
        total_votes += 1

print(f"Total Votes: {total_votes -1}")


# A complete list of candidates who received votes
with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyPoll\main.py\election_data.csv") as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')

    Candidates = []
    if csv.Sniffer().has_header:
        next(pypoll_reader)
    for row in pypoll_reader:
        if row[2] not in Candidates:
            Candidates.append(row[2])

print(Candidates)

# The percentage of votes each candidate won
with open(r"C:\Users\chelb\Documents\GitHub\python_challenge\PyPoll\main.py\election_data.csv") as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')

    Candidates = []
    if csv.Sniffer().has_header:
        next(pypoll_reader)
        
# The total number of votes each candidate won

# The winner of the election based on popular vote.

    