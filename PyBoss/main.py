# # I tested on employee_data1.csv and employee_data2.csv,just need to change the filename and run the script. 
# # Output are saved as output_filename at the same directory with this script.
# # If you want to run anothe raw data file, make sure you store the data in the filepath:../PyPoll/raw_data
# # The file path of this script is at ../PyPoll
# # If you saved data and script at different directories, make sure you make corresponding change on the filepath in the script



#________________________________________________________________________
#PartI import csv,os, and datetime modules 
# I am going to use datetime modules for date conversion
#________________________________________________________________________
import csv
import os
import datetime
#__________________________________________________________________________
#PartII write a function called states_abbreviation(fullname)
#This function takes the full name of a state and return the abbreviation name of 
#that state. e.g. states_abbreviation("Texas") will return "TX"
#__________________________________________________________________________
def states_abbreviation(fullname):
    #use the dictionary with key of states' full name and value of the abbreviations
    #dictionary link is https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
    #By the way, big thanks to who makes and shares this dictionary
    us_state_abbrev ={
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}
    abbreviation=fullname
    for key in us_state_abbrev.keys():
        if fullname==key:
            abbreviation=us_state_abbrev[key]
    return abbreviation

#__________________________________________________________________________
#PartIII Read raw file row by row and write the output file row by row
#__________________________________________________________________________

#Assign filename and filepath
filename="employee_data2.csv"
filepath=os.path.join("raw_data",filename)

#Create an output file name as output_filename
output_file=open("output_"+filename, "a", newline="")
output_writer = csv.writer(output_file)
#write the header for the output file
output_writer.writerow(["Emp ID", "First Name", "Last Name", "DOB","SSN", "State"])
#read from the raw file
with open(filepath,"r",newline="") as csvfile:
    csvreader=csv.reader(csvfile)
    
    #skip the header
    next(csvreader,None)
    for row in csvreader:
        #assign row[0] to a variable as ID
        ID=row[0]

        #split row[1] by " " and assign the first item in the row[1].split as the First_Name 
        #second item in row[1].split as the Last_Name
        First_Name=row[1].split(" ")[0]
        Last_Name=row[1].split(" ")[1]

        #Convert the old date formated as"YYYY-MM-DD" into DD/MM/YYYY 
        DOB=datetime.datetime.strptime(row[2],"%Y-%m-%d").strftime("%d/%m/%Y")

        #convert the old SSN number into format ***-**-321
        SSN="***-**"+row[3][6:]

        #pass the full name of the states in row[4] into the function states_abbreviation to get the 
        #abbreviated name
        State=states_abbreviation(row[4])

        #Combine ID,First_Name,Last_Name,DOB,SSN,State as a list named line
        line=[ID,First_Name,Last_Name,DOB,SSN,State]

        #Writ each line into the output file
        output_writer.writerow(line)
#Close the output_file
output_file.close()