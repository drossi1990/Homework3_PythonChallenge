
import os
import csv
from statistics import mean

#sets file to location of budget data csv
file = 'Resources/budget_data.csv'

#Establishes variables for use in main for loop
#records net profit across the worksheet
Net_profit_loss = 0
#counts rows iterated through to track # of months in worksheet
Row_count = 0 
#variable set to profit for a given row
Profit = 0
#variable set to change in profit from last row
Last_Change_Profit=0 
#variable set to change in profit from current row
Change_Profit = 0
#establishes list to track changes in profit across entire worksheet
Profit_Change_List = []
#establishes list to track dates of profit changes, index values matched to Profit_Change_List
Date_List = []

#reads through .csv input file for main for loop
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #iterates through each row, populates list of profit changes and matching dates across worksheet
    for row in csvreader:
        #records revenue from row 
        Profit = int(row[1])
        #subtracts period profit from last periods
        Change_Profit = (Profit - Last_Change_Profit)
        #appends change to list
        Profit_Change_List.append(Change_Profit)
        #records date of change in a date list which can be referenced in output 
        Date_List.append(row[0])
        #sets Last_Change_Profit value to current rows value for next iteration
        Last_Change_Profit = Profit
        #adds period revenue to total for summary statistic data
        Net_profit_loss = (Net_profit_loss + Profit)
        #tracks row count for number of month output 
        Row_count = (Row_count + 1)
   
#removes first value from profit change list to eliminate calculation error of list average
Profit_Change_List = Profit_Change_List[1:]

#Finds largest positive change in profit found in the worksheet
Greatest_Increase = max(Profit_Change_List)
#uses matching indices to find date of greatest change in profit
Greatest_Increase_Date = Date_List[Profit_Change_List.index(Greatest_Increase)]
#splits greatest positive change into list for reformatting date in output
Greatest_Increase_Date_re = (Greatest_Increase_Date.split('-'))

#Finds largest negative change in profit found in the worksheet
Greatest_Decrease = min(Profit_Change_List)
#uses matching indices to find date of greatest loss in profit
Greatest_Decrease_Date = Date_List[Profit_Change_List.index(Greatest_Decrease)]
#splits greatest negative change into list for reformatting date in output
Greatest_Decrease_Date_re = (Greatest_Decrease_Date.split('-'))

#finds average of profit change across the list, rounds to 2 decimal places for output
Average_Change = round(mean(Profit_Change_List), 2)

#writes properly formatted output data to text file
with open("budget_data.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {Row_count}", file=text_file)
    print(f"Total: ${Net_profit_loss}", file=text_file)
    print(f"Average Change: ${Average_Change}", file=text_file)
    print(f"Greatest Increase in Profits: {Greatest_Increase_Date_re[1]}-20{Greatest_Increase_Date_re[0]} (${Greatest_Increase})", file=text_file)
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date_re[1]}-20{Greatest_Decrease_Date_re[0]} (${Greatest_Decrease})", file=text_file)

#reads data from text file to output in the terminal
with open("budget_data.txt", "r") as text_file:
    for line in text_file:
        print(line)






