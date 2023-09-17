import os
import csv 

#Defining variables to be used later
rowcount = 0 
candidate_list = []
ballot_list = []
candidate_dict = {
    "Candidate":"fname lname",
    "Percentage": 1,
    "Total_votes": 1,
}
ballot_dict = {
    "Ballot_ID": "ballot_id",
    "Candidate_vote": "fname_lname",
    "Candidate_count": 0,
}
#Read the election_data.csv file from python-challenge/Starter_code_PyPoll
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #notifying python that the csv file has a header for the data
    csv_header= next(csvreader)
    #print(csv_header)

    #Find the total number of votes casted  
    for ballot,county,candidate in csvreader:
        rowcount = rowcount + 1   
       
        
    #Complete list of candidates who received votes
        if candidate_list.count(candidate) == 0:
            candidate_list.append(candidate)
            
        #Count the votes as you check each row for each candidate and input that number into the dictionary
        
            #print(f"{candidate} vote is {candidate_vote}")
#Percentage of votes each candidate won

#Total number of votes each candidate won 

#Winner of the election based on popular votes

 #Print the info on terminal
    print(f"Total votes: {rowcount}")
    print(f"The list of candidate who recieved vots {candidate_list}")
    print(f"ballot IDs {ballot_list}")

    for candidate in candidate_list:
        print(f"{candidate}, {candidate_vote}")