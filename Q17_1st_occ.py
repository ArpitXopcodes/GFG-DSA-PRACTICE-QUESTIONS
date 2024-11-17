class Solution:
    def firstIndex(self, arr):
        n=len(arr)
        l=0
        r=n-1

        while l < r:
            m = (l+r)//2
            
            if 1 not in arr:
                return -1
            
            elif arr[m]:
                r = m 
            else:
                l = m + 1
    
        return l