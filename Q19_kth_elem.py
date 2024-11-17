class Solution:
    def getKthfromlast(head,k):
        a = head
        while a:
            if k == a.data:
                return len - k 
            a = a.next
        return False