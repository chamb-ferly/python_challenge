#PyPoll

import csv

# The total number of votes cast
total_votes = 0
with open("election_data.csv", 'r') as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')
    next(pypoll_reader)

    for row in pypoll_reader:
        total_votes += 1

print(f"Total Votes: {total_votes}")


# A complete list of candidates who received votes
with open("election_data.csv", 'r') as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter = ',')
    next(pypoll_reader)
    Candidates = []
    for row in pypoll_reader:
        if row[2] not in Candidates:
            Candidates.append(row[2])
        
print(Candidates)
        
# The total number of votes each candidate won

pypoll_dict = csv.DictReader(open("election_data.csv", 'r'))
mydict = []
for line in pypoll_dict:
    mydict.append(line)

import collections
vote_count = collections.Counter(e['Candidate'] for e in mydict)
print(f"Khan: {vote_count['Khan']}")
print(f"Correy: {vote_count['Correy']}")
print(f"Li: {vote_count['Li']}")
OTooley_votecount = vote_count["O'Tooley"]
print(f"O'Tooley: {OTooley_votecount}")


# The percentage of votes each candidate won
Khan_p = round(((vote_count['Khan'] / total_votes) * 100),3)
Correy_p = round(((vote_count['Correy'] / total_votes) * 100),3)
Li_p = round(((vote_count['Li'] / total_votes) * 100),3)
OTooley_p = round(((OTooley_votecount / total_votes) * 100), 5)

print(f"Khan: {Khan_p}%")
print(f"Correy: {Correy_p}%")
print(f"Li: {Li_p}%")
print(f"O'Tooley: {OTooley_p}%")

# The winner of the election based on popular vote.
winner = max(vote_count, key=vote_count.get)
print(f"Winner: {winner}")

# Output

f = open("results.txt","w+")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("-------------------------\n")
f.write(f"Khan: {Khan_p}%  ({vote_count['Khan']})\n")
f.write(f"Correy: {Correy_p}%  ({vote_count['Correy']})\n")
f.write(f"Li: {Li_p}%  ({vote_count['Li']})\n")
f.write(f"O'Tooley: {OTooley_p}%  ({OTooley_votecount})\n")
f.write("-------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("-------------------------\n")

f.close()