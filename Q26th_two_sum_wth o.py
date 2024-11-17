class Solution:
    def getPairs(self, arr):       
        seen = set()
        pairs = set()
        for num in arr:
            target = -num 
            if target in seen:
                pair = tuple(sorted([target,num]))
                pairs.add(pair)
            else:
                seen.add(num)
        val = list(pairs)
        val.sort()
        return val
                    