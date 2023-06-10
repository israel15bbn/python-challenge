import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    records = list(reader)

    months = len(records)
    net_total = 0
    change = []
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

for i, record in enumerate(records):
    net_total += int(record['Profit/Losses'])
    if i > 0:
        prev_record = records[i-1]
        diff = int(record['Profit/Losses']) - int(prev_record['Profit/Losses'])
        change.append(diff)
        if diff > greatest_increase['amount']:
            greatest_increase = {"date": record['Date'], "amount": diff}
        if diff < greatest_decrease['amount']:
            greatest_decrease = {"date": record['Date'], "amount": diff}

average_change = round(sum(change) / len(change), 2)

print("Financial Analysis")
print("----------------------------")
print("Total Months:", months)
print("Net Total:", net_total)
print("Average Change:", average_change)
print("Greatest Increase:", greatest_increase["date"], "($" + str(greatest_increase["amount"]) + ")")
print("Greatest Decrease:", greatest_decrease["date"], "($" + str(greatest_decrease["amount"]) + ")")

with open("newFiles.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Net Total: {net_total}\n")
    text_file.write(f"Average Change: {average_change}\n")
    text_file.write(f"Greatest Increase: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    text_file.write(f"Greatest Decrease: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")