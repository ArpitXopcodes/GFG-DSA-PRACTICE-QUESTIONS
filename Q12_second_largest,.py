class Solution:
    def getSecondLargest(self, arr):
        # # Code Here
        first = second = float('-inf')
        
        
        for num in arr:
            if num > first:
                second = first
                first = num
            
            elif num > second and num != first:
                second = num
        
        
        return second if second != float('-inf') else -1
        # Code Here

        # 1st aproach time complexity error-----------
        # a = []
        # for x in arr:
        #     if x not in a:
        #         a.append(x)
                
        # if len(a) == 1:
        #     return -1
        # else:
            
        #     a.sort(reverse = True)
        #     return a[1]
    
        # second approach very bad logic---------------
        # a = arr.sort(reverse = True)
        # if len(arr) == 1:
        #     return None
        # else:
        #     a = set(arr)
        #     st = ''
        #     for i in arr:
        #         a += i
        #     return st