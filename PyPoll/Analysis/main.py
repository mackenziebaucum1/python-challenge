#Import Modules

import os
import csv

#Import CSV

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    votes = []

    for row in csvreader:
        votes.append(int(row[0]))

#The total number of votes cast

total_votes = len(votes)
print(total_votes)

#A complete list of candidates who received votes

for x in range(2, count(total_votes)):
    count.append((str(total_votes[x]) - str(total_votes[x-1])))

#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.




