#Import OS Module

import os

#Import CSV file

import csv

budget_data = os.path.join("Resources", "budget_data.csv")

#Open and Read CSV file

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# Read header row
    print(f"Header: Financial Analysis {csv_header}")

#Read Each Row After Header 

for row in csvreader:
    print(row)

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#Print the analysis

#Export to text file


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

