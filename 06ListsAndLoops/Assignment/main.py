def count_failing_grades(grades):
    count=0
    for grade in grades:
        if grade<60:
            count=count+1
    return count
print("count_failing_grades")
print("90,48,67,21,80,59,60 ->",count_failing_grades([90,48,67,21,80,59,60]),"failing grades")

####

def count_act_scores(actScores):
    count=0
    for actScore in actScores:
        if 1<=actScore<=36:
            count=count+1
    return count
print("count_act_scores")
print("23,0,37,32,30,29,36,100 ->",count_act_scores([23,0,37,32,30,29,36,100]))

####

def number_sum(numbers):
    total=0
    for number in numbers:
        total=total+number
    return total
print("number_sum")
print("[2,4,6,19,21] ->",number_sum([2,4,6,19,21]))

####

def average_act_score(scores):
    total=0
    validScores=0
    for score in scores:
        if 1<=score<=36:
            total=total+score
            validScores=validScores+1
    return total/validScores
print("average_act_score")
print("5,36,22,29,25,33,0,50,100 ->",average_act_score([5,36,22,29,25,33,0,50,100]))

####

def all_true(items):
    count=0
    for item in items:
        if item==True:
            count=count+1
    if count==len(items):
        return True
    else:
        return False
print("all_true")
print("[True, False] ->", all_true([True,False]))
print("[True,True,True] ->", all_true([True,True,True]))

####

def any_true(items):
    count=0
    for item in items:
        if item==True:
            count=count+1
    if count>0:
        return True
    else:
        return False
print("any_true")
print("[True, False] ->", any_true([True,False]))
print("[True,True,True] ->", any_true([True,True,True]))
print("[False,False] ->",any_true([False,False]))

####

def mostly_true(items):
    trueCount=0
    falseCount=0
    for item in items:
        if item==True:
            trueCount=trueCount+1
        else:
            falseCount=falseCount+1
    if trueCount>falseCount:
            return True
    else:
            return False
print("mostly_true")
print("[True,False,False] ->", mostly_true([True,False,False]))
print("[True,True,True] ->", mostly_true([True,True,True]))

####

def has_vowel(characters):
    vowelCount=0
    for character in characters:
        if character in ["a","e","i","o","u"]:
            vowelCount=vowelCount+1
    if vowelCount>0:
        return True
    else:
        return False
print("has_vowel")
print("[a,g,h,e,v,n] ->",has_vowel(["a","g","h","e","v","n"]))
print("[b,c,d,f,g] ->",has_vowel(["b","c","d","f","g"]))