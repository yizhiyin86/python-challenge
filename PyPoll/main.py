#Part I import csv file and turn it into list
import os
import csv
filename="election_data_1.csv"
filepath=os.path.join("raw_data",filename)
csvlist=[]
with open(filepath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        csvlist.append(row)
csvlist_no_header=csvlist[1:]
# # #_________________________________________________
# # #Below is for debugging while coding
# # # print("below is for debug") 
# # # print(csvlist[0])
# # # print(csvlist_no_header[0])
# # # print(len(csvlist))
# # # print(len(csvlist_no_header))
# # #_________________________________________________


#__________________________________________________________________________________________
#PartII two lists: one list for candidate_names and one list for votes each received
#____________________________________________________________________________________________
candidate_names=[]
candidate_votes=[]
for ele in csvlist_no_header:
    if ele[2] not in candidate_names:
        num_votes=1
        candidate_names.append(ele[2])
        candidate_votes.append(num_votes)
    else:
        index_of_candidate=candidate_names.index(ele[2])
        candidate_votes[index_of_candidate]+=1
# # #_______________________________________________________________________________________________________
# # #Below is for debugging while coding
# # # print(len(csvlist_no_header)==sum(candidate_votes))
# # # print("unique candidate is {} and each of their votes is {}".format(candidate_names,candidate_votes))
# # #________________________________________________________________________________________________________

#__________________________________________________________________________________________
#PartIII calculate total votes, and create a list to store percentage of votes each candidate win
# ____________________________________________________________________________________________
total_votes=sum(candidate_votes)
winner=candidate_names[candidate_votes.index(max(candidate_votes))]
votes_percentage_list=[]
i=0
while i<len(candidate_votes):
    percentage=candidate_votes[i]/total_votes
    votes_percentage_list.append(percentage)
    i+=1

#__________________________________________________________________________________________
#PartIV output
# ____________________________________________________________________________________________
print("__________________________________\nTotal Votes: "
+str(total_votes)+"\n__________________________________")
j=0
while j<len(candidate_names):
    print(str(candidate_names[j])+": "+"{:.2%}".format(votes_percentage_list[j])
    +" ({})".format(candidate_votes[j]))
    j+=1
print("__________________________________\nWinner: {}\n__________________________________".format(winner))