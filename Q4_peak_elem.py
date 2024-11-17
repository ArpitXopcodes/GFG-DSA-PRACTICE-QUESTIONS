class Solution:
    def peakelement(self,arr,n):
        if n == 0:
            return None
        
        if arr[0]>arr[1]:
            return arr[0]
        
        if arr[n-1]>arr[n-2]:
            return arr[n-1]

        for i in range(1,n-1):
            if arr[n] > arr[n-1] and arr[n]> arr[n+1]:
                return arr[i]
            else:
                return False

solution = Solution()

arr = [1,2,3]
n=3

peak = solution.peakelement(arr,n)

print(peak)