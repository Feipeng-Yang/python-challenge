# Election result analysis for the data in "election_data.csv"
# import modules
import os
import csv

# read data from "election_data.csv"
election_data = os.path.join("Resources", "election_data.csv")

# initialize variables
candidate_list = []
total_votes = 0


with open(election_data) as VotingResult:
    votes = csv.reader(VotingResult, delimiter = ',')

    # read the header row
    votes_header = next(votes)

    # read each row of data after the first row, count total votes and candidate list
    for row in votes:
        # count total votes
        total_votes += 1

        # construct a list that contains all the candidates: candidate_list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])


# -----------read each row in the file again, count votes for each candidate------------
# define a list (with same length as candidate_list) to hold the votes for each candidate
vote_list =[0] * len(candidate_list)

with open(election_data) as VotingResult:
    votes = csv.reader(VotingResult, delimiter = ',')

    # read the header row
    votes_header = next(votes)

    for row in votes:
        # add 1 to the candidate's vote
        candidate = row[2]
        vote_list[candidate_list.index(candidate)] += 1     # index of the candidate that got the vote in this row

##--------  print results to terminal ----------
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# print the list of candidate and their election results
for i in range(len(candidate_list)):
    percentage = "{:.3%}".format(vote_list[i]/total_votes)

    print(f"{candidate_list[i]}: {percentage} ({vote_list[i]})")

print("-------------------------")
# find out the winner
winner = candidate_list[vote_list.index(max(vote_list))]
# print the winer in the election
print(f"Winner: {winner}")
print("-------------------------")

# Export to txt file ----------------------------------------
# Specify the file to write to
output_path = os.path.join("analysis", "PyPoll_analysis.txt")

with open(output_path, "w") as text_file:
    text_file.write("Election Results")
    text_file.write('\n')
    text_file.write("-------------------------")
    text_file.write('\n')
    text_file.write(f"Total Votes: {total_votes}")
    text_file.write('\n')
    text_file.write("-------------------------")
    text_file.write('\n')

    for i in range(len(candidate_list)):
        percentage = "{:.3%}".format(vote_list[i]/total_votes)
        text_file.write(f"{candidate_list[i]}: {percentage} ({vote_list[i]})")
        text_file.write('\n')
    text_file.write("-------------------------")
    text_file.write('\n')
    text_file.write(f"Winner: {winner}")
    text_file.write('\n')
    text_file.write("-------------------------")
    text_file.write('\n')



