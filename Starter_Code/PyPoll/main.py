#importing libaries 
import os
import csv 

#Defining variables to be used later
rowcount = 0 
votecount = []
votecount_list = []
candidate_list = []
per_list = []

#Read the election_data.csv file from python-challenge/Starter_code_PyPoll
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #notifying python that the csv file has a header for the data
    csv_header= next(csvreader)

    #Find the total number of votes casted  
    for ballot,county,candidate in csvreader:
        rowcount = rowcount + 1   
       
        
    #Complete list of candidates who received votes
        if candidate_list.count(candidate) == 0:
            candidate_list.append(candidate)

        #adding all the votes for each candidate into one list to be counted
        votecount.append(candidate)
    
#Counting votes of each candidates from votecount list
for i in candidate_list:

    #adding the total vote count for each candidate into a separate list
    votecount_list.append(votecount.count(i))

#Percentage of votes each candidate won, rounded to 3 decimal places
for i in votecount_list:
    per_list.append(round(i/rowcount*100,3))

#Print the info on terminal
print("Election Results",
"\n-----------------------",
f"\nTotal votes: {rowcount}",
"\n-----------------------\n")

#add info into a dictonary 
candidate_dict = {
    "Candidate": candidate_list,
    "Percentage": per_list,
    "Total votes": votecount_list
}
#For each candidate, find their name, percentage of votes and total votes
for i in range(len(candidate_list)):
    
    #Prints the candidate summary onto terminal
    print(f"{candidate_dict['Candidate'][i]}: {candidate_dict['Percentage'][i]}% ({candidate_dict['Total votes'][i]})")
    
#Find the winner
winner_percent = max(per_list)
index = per_list.index(winner_percent)

#Print out winner
print(f"------------------\n",
f"Winner: {candidate_list[index]}",
"\n---------------------")

##Print everything onto a .txt file

#Create a path for where the .txt file shall be located
output_path = os.path.join("analysis","Election Result.txt")

#Open/Creates the .txt file to be written in
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ' ')
    
    #Create a list to insert into the .txt file in the desired format
    lines = ["Election Results",
    "\n-----------------------",
    f"\nTotal votes: {rowcount}",
    "\n-----------------------\n"
    ]
    #Writes list of information into the .txt file. 
    csvfile.writelines(lines)
    
    #Create a list that contains candidate summary for each candidate
    for i in range(len(candidate_list)):
        lines = (f"{candidate_dict['Candidate'][i]}: {candidate_dict['Percentage'][i]}% ({candidate_dict['Total votes'][i]})",
        "\n")
        #Write the candidate summary for each candidate 
        csvfile.writelines(lines)

    #Create a new list of lines to be inserted into the .txt file
    #This display the winner info in the .txt file.
    lines = [f"------------------\n",
    f"Winner: {candidate_list[index]}",
    "\n---------------------"]
   
   #Writes the new lines into the .txt file
    csvfile.writelines(lines)