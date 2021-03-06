# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The windder of the election based on popular vote.

# Dependencies
import csv
import os
# Assign a variable for the file to load from the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Create a filename variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1 Total number of votes cast
total_votes = 0
# Candidate Options
candidate_options = []
#1. Declare the empty dictionary
candidate_votes = {}
# Track winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
     # Read and print the header row
    headers = next(file_reader)
    #Print eaach row in the CSV file
    for row in file_reader:
       #2 Add to the total vote count
        total_votes += 1
        #Print candidate names
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list 
            candidate_options.append(candidate_name)
            #2. And start tracking the candidate's votes
            candidate_votes[candidate_name] = 0
        # Count the candidate votes
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
#Determine the percentage of voters for each candidate by looping through the counts.
#1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retreive vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)