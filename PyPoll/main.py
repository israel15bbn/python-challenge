import os
import csv
from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_votes = Counter()
candidates = set()

with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_votes += 1
        candidate = row['Candidate']
        candidates.add(candidate)
        candidate_votes[candidate] += 1

percentages = {candidate: round(votes / total_votes * 100, 3) for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in percentages.items():
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("newfile.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, percentage in percentages.items():
        text_file.write(f"{candidate}: {percentage}% ({candidate_votes[candidate]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")