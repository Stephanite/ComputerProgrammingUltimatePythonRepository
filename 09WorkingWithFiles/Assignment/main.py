import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f=open("../data/4000-most-common-english-words.csv", "r")
words=f.read().split("\n")
f.close()

####

def word_with_most_vowels(wordlist):
    mostSoFar=0
    vowelCount=0
    vowels="aeiou"
    mostVowelsWord=""
    for word in wordlist:
        for letter in word:
            if letter in vowels:
                vowelCount=vowelCount+1
            else:
                pass
        if vowelCount>mostSoFar:
            mostVowelsWord=word
    return mostVowelsWord
print("word with most vowels: ", word_with_most_vowels(words))

####

def average_word_length(wordlist):
    wordLengthCount=0
    for word in wordlist:
        wordLengthCount=wordLengthCount+len(word)
    return wordLengthCount/4000
print("average word length: ",average_word_length(words))

####

def most_common_starting_letter(wordlist):
    mostCommonSoFar=ord("")
    commonLetterCount=0
    for word in wordlist:
        firstLetter=ord(word[0])
        if firstLetter==mostCommonSoFar:
            commonLetterCount=commonLetterCount+1

 ####

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 

def number_of_abcdf_awarded():
    for row in reader:
        name, gradelevel, percent=row
        averages="A:",countA,"B:",countB,"C:",countC,"D:",countD,"F:",countF
        percent=int(percent)
        countA=0
        countB=0
        countC=0
        countD=0
        countF=0
        if percent>=90:
            countA=countA+1
        elif percent>=80:
            countB=countB+1
        elif percent>=70:
            countC=countC+1
        elif percent>=60:
            countD=countD+1
        elif percent<=59:
            countF=countF+1
    return averages
print(number_of_abcdf_awarded(reader))

f.close()