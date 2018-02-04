#______________________________________________________________________
#if you want to test paragraph_2.txt in the raw_data folder, just need to change the filename variable
#Note the relative path of this main.py script and the file it will run on
#Please make corresponding change in the filepath if your text file is not under \raw_data\filename
# ____________________________________________________________________________________________________
import re
import os

#assign filename and filepath
filename='paragraph_1.txt'
filepath=os.path.join('raw_data',filename)

#read files
with open(filepath,'r') as text:
    textreader=text.read()

    #_________________________________________________________________________________
    #Rules I use to define a word:
    #1. Words are made up by at least one or more letters e.g. 'apples','a','a1'
    #2. Only numbers or other non-letter symbols are not considered as words, 
    #   so '>1' in paragraph_1.txt is not considered as a word
    #3. Hyphenated words are considered as one word e.g. "high-throughput", "big-data-based"
    #   each is just one word
    # _________________________________________________________________________________________
    #Create a rough WordList by using the pattern '[a-zA-Z]+' to search in textreader
    #Note I do not use'\w+' because I do not want to include numbers as words
    #Note In the WordList hyphenated words will be listed in this way (e.g.):
    #   'ab-cd' as 'ab', 'cd' as two items
    #   'ab-cd-ef' as 'ab','cd','ef' as three items
    #So the accurate count of words will be len(WordList) substract the number 
    # of hyphens in hyphenated words
WordList=re.findall('[a-zA-Z]+',textreader)
# # # print('debug the word list is {}'.format(WordList))
#extract hyphens in hyphenated words by using the pattern '[a-zA-Z]-' to search in the textreader
HyphensInWords=re.findall('[a-zA-Z]-',textreader)
#Calculate the WordCount 
WordCount=len(WordList)-len(HyphensInWords)
# # # print("debug the WordCount is {}".format(WordCount))

#Count Sentence______________________________________________________
#I modified the snipped provided on the homework instruction by expanding characters followed by [.!?] 
# to [\s,"] to include \n and sentence ended by a quotation. That solves most problems for paragraph_2.txt
#except I still found it split 1 more sentence for paragraph_2.txt
#  (it has 10 sentences according to my mannual count)
#It turns out my code split name 'Anne V. Coates,' at the '. ' as well.
#I tried to use regular expression to filter those corner cases out but I could not figure it out
sentenceEnders=re.compile('(?<=[.!?])[\s,"]+')
#split each sentence from the textreader as an item in a list named sentenceList
sentenceList= sentenceEnders.split(textreader)
#Approximate sentence count
senteceCount=len(sentenceList)
#Count Letters_____________________________________________
LetterList=re.findall('[a-zA-Z]',textreader)
LetterCount=len(LetterList)
# # # print("debug the lettercount is {}".format(LetterCount))

# calculate average letter count per word
average_letter_count=LetterCount/WordCount
    
#calculate average sentence lenth in words
average_sentence_lenth=WordCount/senteceCount

#________________________________________________________
#print on the terminal and output into a txt file as well
#________________________________________________________
message=("\nParagraph Analysis \n"+"__________________________________________\n"+"Approximate Word Count: {}".format(WordCount)
    +"\nApproximate Sentence Count: {}".format(senteceCount)+"\nAverage Letter Count: {}".format(average_letter_count)
    + "\nAverage Sentence Length: {}".format(average_sentence_lenth))
print(message)

output_filename=filename[:-3]+"txt"
with open(output_filename,"w") as text:
    text=text.write(message)  


    

