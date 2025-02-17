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
    if validScores==0:
        return None
    else:
        return total/validScores

print("average_act_score")
print("5,36,22,29,25,33,0,50,100 ->",average_act_score([5,36,22,29,25,33,0,50,100]))
print("40 ->", average_act_score([40]))
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

####

def all_the_same(integers):
    lastItem=integers[0]
    for integer in integers:
        if integer==lastItem:
            lastItem=integer
        else:
            return False
    return True
print("all_the_same")
print("[1,2,1] ->", all_the_same([1,2,1]))
print("[4,4,4] ->", all_the_same([4,4,4]))  

####

def increasing(integers):
    previousItem=integers[0]-1
    for integer in integers:
        if integer>previousItem:
            previousItem=integer
        elif integer==previousItem:
            return False
        else:
            return False
    return True
print("increasing")
print("[1,2,5] ->", increasing([1,2,5]))
print("[4,2,3] ->", increasing([4,2,3]))

####

def is_incrementing(integers):
    lastItem=0
    for integer in integers:
        if integer==lastItem+1:
            lastItem=integer
        else:
            return False
    return True
print("is_incrementing")
print("[1,2,3] ->",is_incrementing([1,2,3]))
print("[6,8,10] ->",is_incrementing([6,8,10]))

####

def has_adjacent_repeat(integers):
    repeat=integers[0]-1
    for integer in integers:
        if integer==repeat:
            return True
        else:
            repeat=integer
    return False
            

    #return True
print("has_adjacent_repeat")
print("[2,3,4,4,5] ->", has_adjacent_repeat([2,3,4,4,5]))
print("[3,4,5,7] ->", has_adjacent_repeat([3,4,5,7]))

####

def sum_with_skips(numbers):
    sum=0
    ignore=False
    for number in numbers:
        if ignore == False and number==-1:
            ignore=True
        elif ignore==True and number==-1:
            ignore=False
        elif ignore==False:
            sum=sum+number
    return sum
print("sum_with_skips")
print("[3,-1,4,4,6,-1,4] ->",sum_with_skips([3,-1,4,4,6,-1,4]))
print("[1,1,1] ->", sum_with_skips([1,1,1]))