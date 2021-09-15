# Finacial record analysis for the data in "budget_data.csv"
# import modules
import os
import csv

# Read data from "budget_data.csv"
budget_data = os.path.join('Resources', 'budget_data.csv')

print("Finanicial Analysis")
print("-------------------------")

# Initialize variables
months = 0
total = 0
greatest_increase_amount = 0
greatest_decrease_amount = 0

with open(budget_data) as budget:
    data = csv.reader(budget, delimiter=",")
    # print(data)
    # Read the header row
    data_header = next(data)
    previous_month = next(data)
    first_month = previous_month
    months += 1
    # print(f"Header: {data_header}")
    # print(previous_month)
    total += int(previous_month[1])

    # Read each row of data after the first row
    for row in data:
        # Add budget for total
        total += int(row[1])
        months += 1
        # print(row)
        current_month = row
        change = int(current_month[1]) - int(previous_month[1])

        # update greatest increase and greatest decrease
        if change > greatest_increase_amount:
            greatest_increase_month = current_month[0]
            greatest_increase_amount = change
        if change < greatest_decrease_amount:
            greatest_decrease_month = current_month[0]
            greatest_decrease_amount = change

        # update the last month profit/losses
        previous_month = row
        last_month = row

    # Calculate and display the changes over the entire period 
    average_change = (int(last_month[1])-int(first_month[1]))/(months-1)
    format_average_change = "{:.2f}".format(average_change)

    # Print results to terminal
    print(f"Total Month: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${format_average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")

# Export to csv file ----------------------------------------
# Specify the file to write to
output_path = os.path.join("analysis", "PyBank_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the results to the csv file
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Months:", months])
    csvwriter.writerow(["Total:", '${}'.format(total)])
    csvwriter.writerow(["Average Change", '${}'.format(format_average_change)])
    csvwriter.writerow(["Greatest Increase in Profits:", greatest_increase_month, '${}'.format(greatest_increase_amount)])
    csvwriter.writerow(["Greatest Decrease in Profits:", greatest_decrease_month, '${}'.format(greatest_decrease_amount)])



