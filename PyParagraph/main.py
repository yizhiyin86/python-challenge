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
    print(WordList)
    #extract hyphens in hyphenated words by using the pattern '[a-zA-Z]-' to search in the textreader
    HyphensInWords=re.findall('[a-zA-Z]-',textreader)
    #Calculate the WordCount 
    WordCount=len(WordList)-len(HyphensInWords)
    print(WordCount)

    #Count Sentence______________________________________________________
    #assign sentenceEnders I found this useful snippet at the link below
    #http://pythonicprose.blogspot.com/2009/09/python-split-paragraph-into-sentences.html
    #Thanks to the author for sharing it
    sentenceEnders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
    
    #split each sentence from the textreader as an item in a list named sentenceList
    sentenceList= sentenceEnders.split(textreader)

    #Approximate sentence count
    senteceCount=len(sentenceList)
    print(senteceCount)

    #Count Letters_____________________________________________
    LetterList=re.findall('[a-zA-Z]',textreader)
    print(len(LetterList))
    


    

