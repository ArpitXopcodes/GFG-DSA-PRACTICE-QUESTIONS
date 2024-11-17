class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        a = set(arr1)
        b = set(arr2)
        c = set(arr3)
        
        result =  a.intersection(b.intersection(c))
        
        if result:
            return result
        else :
            return []
        
        