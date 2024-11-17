a1 = {11, 7, 1, 13, 21, 3, 7, 3}
a2 = {11, 3, 7, 1, 7}
# def isSubset(a1, a2,m,n):
#     set_a1 = set(a1)
#     set_a2 = set(a2)
#     n = len(set_a1)
#     m = len(set_a2)
#     return "Yes" if set_a2.issubset(set_a1) else "No"

def isSubset( a1, a2, n, m):
    
    for x in a2:
        if a1.count(x) < a2.count(x):
            return 'No'
        elif a1.count(x)>=a2.count(x):
            if x in a1:
                pass
            else:
                return 'No'
    return 'Yes'
    



