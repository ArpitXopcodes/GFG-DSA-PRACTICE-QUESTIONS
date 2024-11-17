class Solution:
    def leaders(self, arr):
        # code here
        # x = []
        # for i in range(len(arr)-1):
        #     for n in range(len(arr)-1)
        #         if arr[i] > arr[i+n]:
        #             x.append(arr[i])
                       
        #     if x[-1] != arr[-1]:
        #         x.append(arr[-1])
        # return x
    
    
        x = []
        max = arr[-1]
        for i in arr[::-1]:
            if max <= i:
                max = i
                x.append(max)
        return x[::-1]