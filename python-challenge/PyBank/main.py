import csv
import os

file = os.path.join("budget_data.csv")

with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    prev_rev = 0
    rev_change_list = []
 
    rev_change = float(row[1]) - (prev_rev)
    prev_rev = float(row[1])
    rev_change_list = rev_change_list + [rev_change]
 
    rev_change_list.pop(0)    
    rev_avg = sum(rev_change_list)/len(rev_change_list)