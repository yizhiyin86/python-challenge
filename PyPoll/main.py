# # I tested on election_data_1.csv and election_data_2.csv,just need to change the filename and run the script. 
# # Output are saved as filename.txt at the same directory with this script.
# # If you want to run anothe raw data file, make sure you store the data in the filepath:../PyPoll/raw_data
# # The file path of this script is at ../PyPoll
# # If you saved data and script at different directories, make sure you make corresponding change on the filepath in the script


# # ________________________________________________________________________________________
# #Part I import csv file, turn it into list, note that I skipped the header 
# #__________________________________________________________________________________________
import os
import csv
filename="election_data_1.csv"
filepath=os.path.join("raw_data",filename)
csvlist=[]
with open(filepath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #skip the header
    next(csvreader,None)
    #convert each row into a item in the list
    for row in csvreader:
        csvlist.append(row)
# # #_________________________________________________
# # #Below is for debugging while coding
# # # print("below is for debug")
# # # print(csvlist[0])
# # # print(csvlist[0])
# # # print(len(csvlist))
# # # print(len(csvlist))
# # #_________________________________________________


#__________________________________________________________________________________________
#PartII two lists: one list for candidate_names and one list for votes each received
#____________________________________________________________________________________________
candidate_names=[]
candidate_votes=[]

#Loop in the csvlist
for ele in csvlist:
    #check if the candidate is recorded in the candidate_name list

    #if the candidate name is not in the name list, initiate the num of votes as 1 in the voting list.
    # Note that the name and the votes of the same candidate has the same index in each list
    if ele[2] not in candidate_names:
        num_votes=1
        candidate_names.append(ele[2])
        candidate_votes.append(num_votes)
    #if the candidate is in the name list, find her/his index in the candidate_name as index_of_candidate
    # then add 1 to candidate_votes[index_of_candidate]
    else:
        index_of_candidate=candidate_names.index(ele[2])
        candidate_votes[index_of_candidate]+=1
# # #_______________________________________________________________________________________________________
# # #Below is for debugging while coding
# # # print(len(csvlist)==sum(candidate_votes))
# # # print("unique candidate is {} and each of their votes is {}".format(candidate_names,candidate_votes))
# # #________________________________________________________________________________________________________

#_________________________________________________________________________________________________
#PartIII calculate total votes, and create a list to store percentage of votes each candidate wins
# _________________________________________________________________________________________________
total_votes=sum(candidate_votes)
winner=candidate_names[candidate_votes.index(max(candidate_votes))]
votes_percentage_list=[]

#create a list to store percentage of votes that each candidate wins
i=0
while i<len(candidate_votes):
    percentage=candidate_votes[i]/total_votes
    votes_percentage_list.append(percentage)
    i+=1

#__________________________________________________________________________________________
#PartIV output on terminal as well as onto a filename.txt file
# ____________________________________________________________________________________________

#open and append the output_txt file with the name filename(i defined early).txt
output_txt=open(filename[:-3]+"txt","a")

#print lines before the candidate information on terminal and write it into the output_file
print("__________________________________\nTotal Votes: "
+str(total_votes)+"\n__________________________________\n")

output_txt.write("__________________________________\nTotal Votes: "
+str(total_votes)+"\n__________________________________\n")

#Use a loop to print each candiate's information on terminal and to the output file.
j=0
while j<len(candidate_names):
    message=(str(candidate_names[j])+": "+"{:.2%}".format(votes_percentage_list[j])
    +" ({})".format(candidate_votes[j])+"\n")
    print(message)
    output_txt.writelines(message)
    j+=1

#Print and write the last few lines
print("__________________________________\nWinner: {}\n__________________________________".format(winner))
output_txt.write("__________________________________\nWinner: {}\n__________________________________".format(winner))

#Close the output file
output_txt.close()

