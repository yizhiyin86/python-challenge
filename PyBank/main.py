#This python script works for any csv file with two column that the
#first column as the date and the second column as the revenue. I notice that
# the two original files are in time order already. So this script 
#takes advantage of that. Future coding needs to be done to deal with csv files that have not been
#sorted by dates.

#To run a another csv file of the same kind, just change the variable 
#filename="your_file_name.csv" note the file has to be in the direction PythonBank/raw_data
#for this homework, just change to filename="budget_data_1.csv" to run budget_data_2.csv

#Part I 
# ______________________________________________________________
# import csv and convert csv into a list called csv_list_no_header
#________________________________________________________________
import csv
import os
filename="budget_data_2.csv"
csvpath=os.path.join("raw_data", filename)
csv_list=[]
with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        csv_list.append(row)
csv_list_no_header=csv_list[1:]

#Part II
# ____________________________________________________________ 
# calculate the number of months as well as the total revenue
# ____________________________________________________________
num_of_month=len(csv_list_no_header)

#Calculate total revenue
total_revenue=0
for ele in csv_list_no_header:
    total_revenue+=int(ele[1])
# # print("debug "+total_revenue)

#Part III 
#__________________________________________________________
# create another list to store change of revenue by month 
#this list is named as change_by_month_list
#__________________________________________________________
change_by_month_list=[]
i=1
while i<=(len(csv_list_no_header)-1):
    change_by_month=int(csv_list_no_header[i][1])-int(csv_list_no_header[i-1][1])
    change_by_month_list.append(change_by_month)
    i+=1
# # print("debug "+len(change_by_month_list))
# # print("debug "+change_by_month_list[-1])
#
# PartIV
# ________________________________________________________________
# calculate the average_revenue_change
# find the greatest changes of revenue in the change_by_month_list
# and the index number of the greatest changes of the revenue
# use the index number of the greatest increase and decrease to 
# access the corresponding date from the csv_list_no_header
#________________________________________________________________

#Calculate the average of revenue change by month
average_revenue_change=sum(change_by_month_list)/len(change_by_month_list)

#find the greatest increase revenue and its index number
greatest_increase=max(change_by_month_list)
index_increase=change_by_month_list.index(greatest_increase)

# find the greatest decrease of revenue and its index number
greatest_decrease=min(change_by_month_list)
index_decrease=change_by_month_list.index(greatest_decrease)

# # print("debug {},{},{},{}".format(greatest_increase,index_increase,greatest_decrease,index_decrease))

#retrieve the corresponding dates with greatest increase or decrease from 
#csv_list_no_header
Date_greatest_increase=csv_list_no_header[index_increase+1][0]
Date_greatest_decrease=csv_list_no_header[index_decrease+1][0]
# # print("debug "+Date_greatest_increase)
# # print("debug "+Date_greatest_decrease)

#Part V print the ouput in the terminal and create a text
# ____________________________________________________________
#I am using a module sys
#_____________________________________________________________
message=("\nFinancial Analysis \n"+"__________________________________________\n"+"Total months: "
    +str(num_of_month)+"\nTotal Revenue: $"+str(total_revenue)+
    "\nAverage Revenue Change: $"+str(average_revenue_change)+"\nGreatest Increase in Revenue: "
    +str(Date_greatest_increase) + " ($" + str(greatest_increase) +")\nGreatest Decrease in Revenue: "
    +str(Date_greatest_decrease) + " ($" + str(greatest_decrease) +")\n")
print(message)

output_filename=filename[:-3]+"txt"
with open(output_filename,"w") as text:
    text=text.write(message)