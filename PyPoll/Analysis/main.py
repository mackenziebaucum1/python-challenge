#Import Modules
import os
import csv

#Import CSV
election_data = os.path.join("Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#Declare Variables
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""
Khan_votes = 0
correy_votes =0 
li_votes =0
otooley_votes = 0


for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1
	
#candidates who recieved votes
for candidate in candidate_votes:
        if candidate == "Khan":
            khan.append(candidate)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidate)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidate)
            li_votes = len(li)
        else:
            otooley.append(candidate)
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

#Print
with open('output.txt', 'w+') as file:
	file.write("Election Results\n")
	file.write("----------------------------\n")
	file.write("Total Votes: " + str(votes)+"\n")
	file.write("----------------------------\n")
	for candidate in d:
		percent = round(d[candidate]/total_votes * 100,2)
		file.write(candidate +": "+ str(percent) +"%" +" ("+str(d[candidate]) +")\n")
	file.write("----------------------------\n")
	file.write("Election winner: " + winner+"\n")
	file.write("----------------------------\n")
