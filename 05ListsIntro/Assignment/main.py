def make_abc():
    list=["a","b","c"]
    return list
print("make_abc")
print(make_abc())

####

def equal_edges(items):
    first=items[0]
    last=items[-1]
    if first==last:
        return True
    else:
        return False
print("equal_edges")
print("[1,2,1] ->", equal_edges([1,2,1]))
print("[1,2,4] ->", equal_edges([1,2,4]))

####

def common_edge(list1,list2):
    first1=list1[0]
    last1=list1[-1]
    first2=list2[0]
    last2=list2[-1]
    if first1==last2 or last1==first2 or first1==last1 or first2==last2:
        return True
    else:
        return False
print("common_edge")
print("[1,3,5,6],[6,5,4,4] ->", common_edge([1,3,5,6],[6,5,4,4]))
print("[1,3,5,7],[6,5,4,6] ->", common_edge([1,3,5,7],[6,5,4,6]))
print("[7,3,5,6],[6,5,4,7] ->", common_edge([7,3,5,6],[6,5,4,7]))
print("[1,3,5,6],[9,5,4,4] ->", common_edge([1,3,5,6],[9,5,4,4]))

####

def all_the_same(items):
    first,middle,last=items
    if first==middle==last:
        return True
    else:
        return False
print("all_the_same")
print("[1,2,3] ->",all_the_same([1,2,3]))
print("[4,4,4] ->", all_the_same([4,4,4]))

####

def all_unique(items):
    first,middle,last=items
    if first==middle or middle==last or first==last:
        return False
    else:
        return True
print("all_unique")
print("[4,2,4] ->",all_the_same([4,2,4]))
print("[4,6,7] ->", all_the_same([4,6,7]))

####

def increasing(items):
    first,middle,last=items
    if first<middle and middle<last:
        return True
    else:
        return False
print("increasing")
print("[15,16,17] ->", increasing([15,16,17]))
print("[9,8,10] ->", increasing([9,8,10]))

####

def all_true(items):
    first,middle,last=items
    if first==True and middle==True and last==True:
        return True
    else:
        return False
print("all_true")
print("[True,True,True] ->", all_true([True,True,True]))
print("[false,True,false] ->", all_true(["false",True,"false"]))

####

def mostly_true(items):
    first,middle,last=items
    if first==True and middle==True:
        return True
    elif middle==True and last==True:
        return True
    elif last==True and first==True:
        return True
    else:
        return False
print("mostly_true")
print("[true,true,false] ->", mostly_true([True,True,False]))
print("[false,true,false] ->", mostly_true([False,True,False]))

####

def make_copy(item):
    first,middle,last=item
    return item
print("make_copy")
print("[3,6,7] ->",make_copy([3,6,7]))

###

def repeat_thrice(item):
    return [item,item,item]
print("repeat_thrice")
print("3 ->", repeat_thrice(3))

####

def make_reversed_copy(original):
    first1,middle1,last1=original
    first2=last1
    middle2=middle1
    last2=first1
    new=[first2,middle2,last2]
    return new
print("make_reversed_copy")
print("[2,3,7] ->",make_reversed_copy([2,3,7]))

####

def reverse_in_place(original):
    first,middle,last=original
    new=[last,middle,first]
    return new
print("reverse_in_place")
print("[5,4,3] ->",reverse_in_place([5,4,3]))