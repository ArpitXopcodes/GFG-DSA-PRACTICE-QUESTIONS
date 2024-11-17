a = [1,3,4,2,4,5,]
class Solution:
    def findDuplicates(self, arr):
        
        # code here
        x = []
        y = {}
        
        for i in arr:
            if i in y:
                y[i] += 1
                if y[i] == 2:
                    x.append(i)
            else:
                y[i] = 1
                
        x.sort()
        return x
            
sol = Solution()
print(sol.findDuplicates(a))