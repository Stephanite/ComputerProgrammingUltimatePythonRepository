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
print("average word length: ",round(average_word_length(words),0))

####

def most_common_starting_letter(wordlist):
    mostCommonSoFar=""
    commonLetterCount=0
    for word in wordlist:
        firstLetter=word[0]
        if firstLetter==mostCommonSoFar:
            commonLetterCount=commonLetterCount+1

 ####

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)
failingSeniors=""
freshmanCount=0
sophmoreCount=0
juniorCount=0
seniorCount=0
freshmanGrades=0
sophmoreGrades=0
juniorGrades=0
seniorGrades=0
countA=0
countB=0
countC=0
countD=0
countF=0
for row in reader:
    name, gradelevel, percent=row
    percent=int(percent)
    gradelevel=int(gradelevel)

    # number of abcdf
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

    # number of faiing seniors
    if gradelevel==12 and percent<60:
        failingSeniors=name+", "+failingSeniors

    # each grade level average percent
    if gradelevel==9:
        freshmanCount=freshmanCount+1
        freshmanGrades=freshmanGrades+percent
    if gradelevel==10:
        sophmoreCount=sophmoreCount+1
        sophmoreGrades=sophmoreGrades+percent
    if gradelevel==11:
        juniorCount=juniorCount+1
        juniorGrades=juniorGrades+percent
    if gradelevel==12:
        seniorCount=seniorCount+1
        seniorGrades=seniorGrades+percent

print("# of A:",countA)
print("# of B:",countB)
print("# of C:",countC)
print("# of D:",countD)
print("# of F:",countF)

freshmanAverage=freshmanGrades/freshmanCount
print("average freshman percent:",round(freshmanAverage,2))
sophmoreAverage=sophmoreGrades/sophmoreCount
print("average sophmore percent:",round(sophmoreAverage,2))
juniorAverage=juniorGrades/juniorCount
print("average junior percent:",round(juniorAverage,2))
seniorAverage=seniorGrades/seniorCount
print("average senior percent:",round(seniorAverage,2))

print("failing seniors:",failingSeniors)

f.close()