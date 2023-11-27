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

def all_the_same(list):
    first,middle,last=list
    if first==middle==last:
        return True
    else:
        return False
print("all_the_same")
print("[1,2,3] ->",all_the_same([1,2,3]))
print("[4,4,4] ->", all_the_same([4,4,4]))

####

def all_unique(list):
    first,middle,last=list
    if first==middle or middle==last or first==last:
        return False
    else:
        return True
print("all_unique")
print("[4,2,4] ->",all_the_same([4,2,4]))
print("[4,6,7] ->", all_the_same([4,6,7]))

####

def increasing(list):
    first,middle,last=list
    if first<middle and middle<last:
        return True
    else:
        return False
print("increasing")
print("[15,16,17] ->", increasing([15,16,17]))
print("[9,8,10] ->", increasing([9,8,10]))

####

def all_true(list):
    first,middle,last=list
    if first=="true" and middle=="true" and last=="true":
        return True
    else:
        return False
print("all_true")
print("[true,true,true] ->", all_true(["true","true","true"]))
