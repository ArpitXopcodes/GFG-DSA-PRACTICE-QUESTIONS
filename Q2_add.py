# code for adding the numbers in set 
def adding(num): #hamne ek function banaya jo hame ye operations multiple time excecute karke dega
    total = 0
    for i in num: # loop ko pure list mai chalaya 
        total +=i  #aur fir hamne isko jo line 3 pe total h usme store kar diya
    return total   

print(adding((1,2,3,4,5)))  #function call kar diya
