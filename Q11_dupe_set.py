class Solution:
	def removeDups(str):
		sett = set(str)
		st = ''
		for i in sett:
			st += i
		return st
    
sol = Solution()
print(Solution.removeDups([2,3,2,4,5,1,6]))