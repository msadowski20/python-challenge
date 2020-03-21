# PyPoll

# Import OS and CSV modules

import os
import csv

# Name the .csv file path
csvpath = os.path.join('election_data.csv')
output_path = ('election_results.txt')

# Declare variables
total_votes = 0
total_candidate_list = []
candidate_list = []
vote_list = []

# Open the .csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Identify the header
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        total_candidate_list.append(row[2])
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])


    for candidate in candidate_list:
        vote_list.append(total_candidate_list.count(candidate))
        
election_dictionary = dict(zip(candidate_list, vote_list))

print(election_dictionary)