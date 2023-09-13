#import libaries 
import os 
import csv 

#Create list to hold rows
months = []
profit_loss_total = []
profit_loss_average = []
# create a path to the necessairly folders while in python-challenge/Starter_Code/PyBank directory 
csvpath = os.path.join('Resources','budget_data.csv')
 

# Display Header in terminal 
print(f"Financial Analysis \n\n----------------------------------------\n")

# We need to be able to read the file first from python
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Separate the columns from each other and put them into their own list. 
    for date, money in csvreader:
        months.append(date)
        profit_loss_total.append(int(money))
    print(f"Total  Months: {len(months)}")

#Calculate the net total of "Profit/Losses" over the entire period   
    total_value = sum(profit_loss_total)
    print(f"This is the total value ${total_value}")


#Calculate the changes in "profit/losses" and then average of those changes.
    for i in range(1, len(profit_loss_total)):
        #difference between months
        diff_month = profit_loss_total[i] - profit_loss_total[i-1]
        profit_loss_average.append(diff_month)
   
    # calculate the average of all the changes
    month_total_average = sum(profit_loss_average) / len(profit_loss_average)
    print(f"Average change: ${month_total_average}")

# Find the greatest increase in profits (date and amount) over the entire period
    profit_max = max(profit_loss_average)
    print(f"Greatest Increase in Profits: {months[profit_loss_average.index(profit_max)+1]}, ${profit_max}")

# Find the greatest decrease in profits (date and amount) over the entire period
    profit_loss= min(profit_loss_average)
    print(f"Greatest Decrease in Profits: {months[profit_loss_average.index(profit_loss)+1]}, ${profit_loss}")

#Display all the results in a .txt file in analysis folder 
