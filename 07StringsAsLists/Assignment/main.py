def is_alliteration(word1,word2):

    firstLetter1=word1[0]
    firstLetter2=word2[0]
    if firstLetter1==firstLetter2:
        return True
    else:
        return False
print("is_allteration")
print("flower and floor ->", is_alliteration("flower","floor"))
print("computer and keyboard ->", is_alliteration("computer","keyboard"))
print("apple and ant ->", is_alliteration("apple","ant"))


####

def count_vowels(word):
    vowelCount=0
    for letter in word:
        if letter in ["a","e" ,"i" ,"o","u"]:
            vowelCount=vowelCount+1
    return vowelCount
print("count_vowels")
print("potato ->", count_vowels("potato"))
print("try ->", count_vowels("try"))

####

def count_numbers(string):
    numberCount=0
    for digit in string:
        if digit in ["1","2","3","4","5","6","7","8","9","0"]:
            numberCount=numberCount+1
    return numberCount
print("count_numbers")
print("h311o ->", count_numbers("h311o"))
print("penguin ->", count_numbers("penguin"))
print("123YO09 ->", count_numbers("123YO09"))

####

def count_target_letters(word,character):
    count=0
    if len(character)==1:
        for letter in word:
            if letter==character:
                count=count+1
        return count
print("count_target_letters")
print("apple, a ->", count_target_letters("apple", "a"))
print("smile, h ->", count_target_letters("smile","h"))

####

def in_alphabetical_order(word):
    alphabet="a"
    for letter in word:
        if letter>=alphabet:
            alphabet=letter
        else:
            return False
    return True
print("in_alphabetical_order")
print("abcdefg ->", in_alphabetical_order("abcdefg"))
print("gjfjnvfdn ->", in_alphabetical_order("gjfjnvfdn"))
