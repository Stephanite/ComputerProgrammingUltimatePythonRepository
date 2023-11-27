def make_abc():
    list=["a","b","c"]
    return list
print(make_abc())

####

def equal_edges(items):
    first=items[0]
    last=items[-1]
    if first==last:
        return True
    else:
        return False
print("[1,2,1] ->", equal_edges([1,2,1]))
print("[1,2,4] ->", equal_edges([1,2,4]))

####

def common_edge(list1,list2):
    first1,middle1,last1=list1
    first2,middle2,last2=list2
    if first1==last2 or last1==first2 or first1==last1 or :
        return True
    else:
        return False
print("[1,3,5,6],[6]")