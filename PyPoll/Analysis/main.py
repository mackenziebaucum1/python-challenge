#Import Modules

import os
import csv

#Import CSV

election_data = os.path.join("Resources", "election_data csv.csv")

#Declare Variables

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidates = []
candidate_votes = {}
county = []
khan = []
correy = []
li = []
otooley = []

with open(election_data, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
# Skip header line
	next(csvreader, None)

#The total number of votes cast

for row in cvsreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

total_votes = (len(votes))
print(total_votes)

#candidates who recieved votes

for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)

#The percentage of votes each candidate won

khan_percent = round(((khan_votes / total_votes) * 100), 2)
correy_percent = round(((correy_votes / total_votes) * 100), 2)
li_percent = round(((li_votes / total_votes) * 100), 2)
otooley_percent = round(((otooley_votes / total_votes) * 100), 2)

print(khan_percent)
print(correy_percent)
print(li_percent)
print(otooley_percent)

#The total number of votes each candidate won

if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
else:
        winner = "O'Tooley"

#Print Results and winner

output_file = os.path.join('election_data' + str(file_num) +'.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
