#import modules needed for reading csv and outputting .txt results
import os
import csv

#file path for csv to read
file = 'Resources/election_data.csv'

#function which returns number of votes for a given candidate
def candidate_votes(candidate):
    with open(file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        vote_count = 0
        next(csvreader)
        for row in csvreader:
            if row[2] == candidate: 
                vote_count = vote_count + 1
        return vote_count 

#reads from csv file to find all unique candidates in csv file, appends candidates to a list
with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    candidate_list = []
    next(csvreader)
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])    

#Establishes dictionary of two lists: names of candidates and votes each received, the latter being found by calling on the candidate_votes function
Candidate_Dictionary = {"Name":[],"Votes":[]}
for candidate in candidate_list:
    Candidate_Dictionary["Name"].append(str(candidate))
    Candidate_Dictionary["Votes"].append(int(candidate_votes(candidate)))
    
#adds all votes from the votes list in the candidate dictionary to find total votes in the election 
Total_Votes = 0
for vote in Candidate_Dictionary["Votes"]:
    Total_Votes = Total_Votes + vote

#writes election results to .txt file in the main.py directory 
with open("Poll_Results.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------------", file=text_file)
    print(f"Total Votes: {Total_Votes}", file = text_file)
    #loop to print percentage of total votes and total votes for each candidate based on dictionary values
    for candidate in Candidate_Dictionary["Name"]:
        Candidate_Vote = Candidate_Dictionary["Votes"][Candidate_Dictionary["Name"].index(candidate)]
        Candidate_Percent = (100*(Candidate_Vote/Total_Votes))
        print(f"{candidate}: {round(Candidate_Percent, 2)}% ({Candidate_Vote})", file = text_file)
    print("-------------------------------", file = text_file)
    winner_votes = max(Candidate_Dictionary["Votes"])
    winner_index = Candidate_Dictionary["Votes"].index(winner_votes)
    winner_name = Candidate_Dictionary["Name"][winner_index]
    print(f"Winner: {winner_name}", file = text_file)

#reads from results text file to print results to the terminal
with open("Poll_Results.txt", "r") as text_file:
    for line in text_file:
        print(line)
