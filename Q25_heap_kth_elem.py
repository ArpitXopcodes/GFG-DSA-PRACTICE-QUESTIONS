import heapq
class Solution:

    def kthSmallest(self, arr,k):
        heapq.heapify(arr)
        ans =-1 
        while(k > 0):
            ans = heapq.heappop(arr)
            k -= 1 
        return ans