#PyPoll

#Import OS and CSV modules
import os
import csv

#Name the .csv file path and output path for text file
csvpath = os.path.join('election_data.csv')
output_path = ('election_results.txt')

#Declare variables and empty lists
total_votes = 0
total_candidate_list = []
candidate_list = []
vote_list = []

#Open the .csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #Identify the header
    csv_header = next(csvreader)

    #Loop through each row in the file and count the total number of votes,
    #add each item in the 'Candidate' column to a list,
    #add each unique value in 'Candidate' column to a list
    for row in csvreader:
        total_votes += 1
        total_candidate_list.append(row[2])
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    #Loop through each candidate and count each of their votes,
    #add those vote counts to a list
    for candidate in candidate_list:
        vote_list.append(total_candidate_list.count(candidate))

#Create a dictionary with the candidates as the keys and vote counts as the values       
election_dictionary = dict(zip(candidate_list, vote_list))

#Set election winner as the max of the election dictionary
election_winner = max(election_dictionary, key=election_dictionary.get)

#Print all of the results
print("Election Results")
print("------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------------------")
for i in election_dictionary:
    print(f"{i}: {format(float(election_dictionary[i] / total_votes), '.3%')} ({election_dictionary[i]})")
print("------------------------------------------------------")
print(f"Winner: {election_winner}")
print("------------------------------------------------------")

#Output the results into a new text file
with open(output_path, 'w') as datafile:

    datafile.write("Election Results\n")
    datafile.write("------------------------------------------------------\n")
    datafile.write("Total Votes: " + str(total_votes) + "\n")
    datafile.write("------------------------------------------------------\n")
    for i in election_dictionary:
        datafile.write(f"{i}: {format(float(election_dictionary[i] / total_votes), '.3%')} ({election_dictionary[i]})\n")
    datafile.write("------------------------------------------------------\n")
    datafile.write(f"Winner: {election_winner}\n")
    datafile.write("------------------------------------------------------\n") 


            