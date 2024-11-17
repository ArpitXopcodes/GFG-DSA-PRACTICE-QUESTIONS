class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d %= n  
        if d == 0:
            return arr
        
        
        arr[:d] = reversed(arr[:d])
        
        
        arr[d:] = reversed(arr[d:])
        
        
        arr[:] = reversed(arr)
        
        return arr
