from ast import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        l = 0
        
        r = n-1
        
        lm = float("-inf")
        
        rm = float("inf")
        
        
        while l <=r:
            
            m = (l+r)//2
            
            num = arr[m]
            
            if num== k:
                
                return num
                
            elif num <k:
                
                lm = num
                
                l = m+1
                
            else:
                
                rm = num
                
                r = r-1
                
                
        
        if rm-k <= k - lm:
            
            return rm
            
        else:
            
            return lm
