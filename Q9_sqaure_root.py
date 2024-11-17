'''sqaure root of a number
first import math for sqrt fn or use n**1/2 as formula 
if sqrt is equal to n then return sqrt value 
else retrun the rounded of square root of the given num with trunc
'''


class Solution:
    def floorSqrt(self, n):
        import math
        if math.sqrt(n) == n:
            return math.sqrt(n)
        else:
            return math.trunc(math.sqrt(n))
        


sol = Solution()
ans= sol.floorSqrt(8)
print(ans)