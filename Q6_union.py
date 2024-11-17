class Solution:    
    def findUnion(self, a, b):
        x = set(a).union(set(b))
        return len(x)

