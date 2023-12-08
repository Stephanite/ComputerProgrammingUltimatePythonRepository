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


print("")

def count_vowels(word):
    vowelCount=0
    for letter in word:
        if letter in ["a","e" ,"i" ,"o","u"]:
            vowelCount=vowelCount+1
    return vowelCount
print("count_vowels")
print("potato ->", count_vowels("potato"))
print("try ->", count_vowels("try"))

print("")

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

print("")

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

print("")

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

print("")

def alternate_case(word):
    result=""
    next_upper= True
    for letter in word:
        if next_upper==True:
            result=result+letter.upper()
            next_upper=False
        elif next_upper==False:
            result=result+letter.lower()
            next_upper=True
    return result
print("alternate_case")
print("computer ->", alternate_case("computer"))
print("pizza ->", alternate_case("pizza"))

print("")

def remove_vowels(string):
    result=""
    for letter in string:
        if letter in "aeiou":
            pass
        else:
            result=result+letter
    return result
print("remove_vowel")
print("teeth ->", remove_vowels("teeth"))
print("bananna ->", remove_vowels("bananna"))
print("sky ->", remove_vowels("sky"))

print("")

def to_camel_case(string):
    result=""
    nextUpper=False
    for letter in string:
        if letter==" ":
            nextUpper=True
        elif nextUpper==True:
            result=result+letter.upper()
            nextUpper=False
        else:
            result=result+letter
    return result
print("to_camel_case")
print("final test today ->", to_camel_case("final test today"))

print("")

def to_snake_case(string):
    result=""
    for item in string:
        if item==" ":
            result= result+item.replace(" ","_")
        else:
            result=result+item
    return result
print("to_snake_case")
print("final test today ->", to_snake_case("final test today"))

print("")

def without_duplicates(numbers):
    result=[]
    previousNumber=numbers[0]-1
    for number in numbers:
        if number==previousNumber:
            previousNumber=number
        else:
            previousNumber=number
            result.append(number)
    return result
print("without_duplicates")
print("[1,2,5,5,7] ->", without_duplicates([1,2,5,5,7]))

print("")

def filter_valid_act_scores(numbers):
    validScore=[]
    for number in numbers:
        if 1<=number<=36:
            validScore.append(number)
        else:
            pass
    return validScore
print("filter_vaild_act_scores")
print("[1,21,90,47,36,30,24,0] ->", filter_valid_act_scores([1,21,90,47,36,30,24,0]))