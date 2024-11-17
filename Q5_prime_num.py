class Solution:
    def isPrime (self,a):
        if a <= 1:
            return False
        for i in range(1,int(a**1/2)+1):
            if a% i ==0:
                 return False
        return True
        

soln = Solution()
a = 5
ans = soln.isPrime(a)
print(ans)
