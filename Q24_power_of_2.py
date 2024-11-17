import math
class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # code here
        for i in range(round(math.sqrt(n))+1):
            if 2 ** i == n:
                return True
                
        return False