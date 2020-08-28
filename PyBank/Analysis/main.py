#Import  Modules

import os
import csv

#Import CSV file

budget_data = os.path.join("Resources", "budget_data.csv")

#Open and Read CSV file

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# Read header row

    print(f"Header: Financial Analysis {csv_header}")

#Read Each Row After Header 

    Profit = []
    months = []

    for row in csvreader:
        Profit.append(int(row[1]))
        months.append(row[0])

#The net total amount of "Profit/Losses" over the entire period

revenue_change = []

for x in range(1, len(Profit)):
    revenue_change.append((int(Profit[x]) - int(Profit[x-1])))

#The average of the changes in "Profit/Losses" over the entire period

revenue_average = sum(revenue_change) / len(revenue_change)

#The total number of months included in the dataset

total_months = len(months)

#The greatest increase in profits (date and amount) over the entire period

greatest_increase = max(revenue_change)

#The greatest decrease in losses (date and amount) over the entire period

greatest_decrease = min(revenue_change)

#Print the analysis

print("Financial Analysis")

print("....................................................................................")

print("total months: " + str(total_months))

print("Total: " + "$" + str(sum(Profit)))

print("Average change: " + "$" + str(revenue_average))

print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

#Export to text file

file = open("output.txt","w")

file.write("Financial Analysis" + "\n")

file.write("...................................................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(Profit)) + "\n")

file.write("Average change: " + "$" + str(revenue_average) + "\n")

file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
