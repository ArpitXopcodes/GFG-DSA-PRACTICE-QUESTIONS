'''sum of the series or sum of n natural number'''
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        return (n * (n + 1)) // 2 
        # it is the basic formula for sum of n natural numbers
