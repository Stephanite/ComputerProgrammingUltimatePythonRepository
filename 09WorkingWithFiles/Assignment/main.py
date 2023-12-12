import csv

f=open("../data/4000-most-common-english-words.csv", "r")
words=f.read().split("\n")
f.close()

def word_with_most_vowels(wordlist):
    mostSoFar=0
    vowelCount=0
    vowels=["a","e","i","o","u"]
    mostVowelsWord=""
    for word in wordlist:
        if vowels in word:
            vowelCount=len(vowels)
        else:
            pass
        if vowelCount>mostSoFar:
            mostVowelsWord=word
    return mostVowelsWord
   # print("word with most vowels: ", mostVowelsWord)
