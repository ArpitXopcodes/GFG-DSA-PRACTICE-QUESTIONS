class Solution:
    def reverseInGroups(self, arr, k):
        a = len(arr)
        for i in range(0, a, k):
            arr[i:i + k] = reversed(arr[i:i + k])
        return arr 
    
    
    
