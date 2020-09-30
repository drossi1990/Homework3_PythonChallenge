import os
import csv

# # A For loop moves through a given range of numbers
# # If only one number is provided it will loop from 0 to that number
# for x in range(10):
#     print(x)

# # If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
# for x in range(20, 30):
#     print(x)

# # If a list is provided, then the For loop will loop through each element within the list
# words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]
# for word in words:
#     print(word)

# # A While Loop will continue to loop through the code contained within it until some condition is met
# x = "Yes"
# while x == "Yes":
#     print("Whee! Merry-Go-Rounds are great!")
#     x = input("Would you like to go on the Merry-Go-Round again? ")


# # Store the file path associated with the file (note the backslash may be OS specific)
file = 'budget_data.csv'
Total_Months = int
Net_profit_loss = int
Average_profit_loss = int
Row_count = int 

Greatest_profit_date = str
Greatest_profit_amount = int

Greatest_loss_date = str
Greatest_loss_amount = int 


# # Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        Net_profit_loss = (Net_profit_loss + row[1])
        Row_count = (Row_count + 1)
        If Greatest_profit_amount < row[1]:
            Greatest_profit_amount = row[1]
            Greatest_profit_date = row[0]
        Elif Greatest_loss_amount > row[1]:
            Greatest_profit_amount = row[1]
            Greatest_profit_date = row[0]
    print
            
#     # This stores a reference to a file stream
    Average_Change = (Net_profit_loss / Row_count)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {Row_count}")
    print(f"Average Change: {Average_Change}")
    print(f"Greatest Increase on Profits: {Greatest_profit_date} ({Greatest_profit_amount})")
    print(f"Greatest Increase on Profits: {Greatest_loss_date} ({Greatest_loss_amount})")


#     # Store all of the text inside a variable called "lines"
#     lines = text.read()

#     # Print the contents of the text file
#     print(lines)
