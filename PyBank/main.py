#PyBank

#Import OS and CSV modules
import os
import csv

#Name the .csv file path and output path for text file
csvpath = os.path.join('budget_data.csv')
output_path = ('financial_analysis.txt')

#Declare variables and empty lists
total_months = 0
total_pl = 0
greatest_increase = 0
greatest_decrease = 0
total_list = []
change_list= []

#Open the .csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Identify the header
    csv_header = next(csvreader)

    #Print the 'Financial Analysis' header as output
    print("------------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------------")

    #Loop through each row in the file and count the total number of months,
    #add each value in the 'Profit/Losses' column to a list as a floating decimal value,
    #sum up all the values in the list to get the total profit/loss and format that value as currency
    for row in csvreader:
        
        #total_pl += float(row[1])
        total_months += 1
        total_list.append(float(row[1]))
        total_pl = sum(total_list)

        total_format = format(total_pl, ",.2f")

        #Loop through each row in the data set to get the greatest increase in profits and greatest decrease in losses,
        #Start counter at 0 and check if each value is greater than the previous value;
        #if so, set that value as greatest_increase and record the corresponding period
        #Start counter at 0 and check if each value is less than the previous value;
        #if so, set that value as greatest_decrease and record the corresponding period
        #Format the results as currency
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            increase_period = row[0]

            increase_format = format(greatest_increase, ",.2f")

        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            decrease_period = row[0]

            decrease_format = format(greatest_decrease, ",.2f") 

    #Loop through the total list starting at the second value,
    #take that value minus the previous value to get the change value add each of those values to a separate list,
    #take the sum of the change list and divide by the length of the list to get the average change
    #Format the result as currency
    for i in range(1, len(total_list)):

        change_list.append(total_list[i] - total_list[i-1])
        average_change = sum(change_list) / len(change_list)

        average_format = format(average_change, ",.2f")     

    #Print out all of the results
    print(f"Total Months: {total_months}")
    print(f"Total Profit/Loss: ${total_format}")
    print(f"Average Change: ${average_format}")
    print(f"Greatest Increase in Profits: {increase_period} $({increase_format})")
    print(f"Greatest Decrease in Losses: {decrease_period} $({decrease_format})")

#Output the results into a new text file
with open(output_path, 'w') as datafile:

    datafile.write("------------------------------------------------------\n")
    datafile.write("Financial Anlysis\n")
    datafile.write("------------------------------------------------------\n")
    datafile.write("Total Months: " + str(total_months) + "\n")
    datafile.write("Total Profit/Loss: $" + str(total_format) + "\n")
    datafile.write("Average Change: $" + str(average_format) + "\n")
    datafile.write("Greatest Increase in Profits: " + increase_period + " $(" + str(increase_format) + ")\n")
    datafile.write("Greatest Decrease in Losses: " + decrease_period + " $(" + str(decrease_format) + ")\n")


