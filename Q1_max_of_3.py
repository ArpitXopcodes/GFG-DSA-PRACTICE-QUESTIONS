def maxofthreenum(a,b,c):
    max = float("-infinity")
    if a>b and a>c:
        max = a
    elif b>a and b>c:
        max = b
    else :
        max = c
    return max

a = int(input("enter 1st number :"))
b = int(input("enter 2nd number :"))
c = int(input("enter 3rd number :"))
result=maxofthreenum(a,b,c)
print(f"the max of three no is {result}")
