# code for multiplying the numbers in set 
def multi(num): #hamne ek function banaya jo hame ye operations multiple time excecute karke dega
    total = 1
    for i in num: # loop ko pure list mai chalaya 
        total *= i  #aur fir hamne isko jo line 3 pe total h usme store kar diya 
    return total  
    
print(multi((2,3,4,5,6,7)))  #function call kar diya