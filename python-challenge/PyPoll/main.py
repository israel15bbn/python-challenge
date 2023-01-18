import csv
import os

file = os.path.join("election_data.csv")

with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    candidates = {}

    for row in csvreader:
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    for key, value in candidates.items():
        print(key, value)
        