from ast import Return


class Solution:
    def findPeakElement(self, a):
        n = len(a)
        l = 0 
        h = len(a)-1
        while l <= h:
            m = l + (h - l) // 2
            if m == len(a)-1:
                return a[m]
            elif a[m] > a[m + 1] and a[m] > a[m - 1]:
                return a[m]
            elif a[m]<a[m + 1]: 
                l = m + 1
            else:
                h = m - 1
        return -1
        

# class Solution:
#     def findPeakElement(self, a):
#         # Code hehe
#         low=0
#         high=len(a)-1
#         while(low<=high):
#             mid=((low+high)//2)
#             if mid==len(a)-1:
#                 return a[mid]
#             elif a[mid]>a[mid+1] and a[mid]>a[mid-1]:
#                 return a[mid]
#             elif a[mid]<a[mid+1]:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return -1
            

