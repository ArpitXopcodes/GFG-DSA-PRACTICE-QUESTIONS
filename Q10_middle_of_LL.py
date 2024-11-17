class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # Code here
        # return the value stored in the middle node
        if not head:
            return -1

        count = 0 
        a = head
        while a:
            count += 1
            a = a.next

        mid = count // 2
        a = head
        for i in range(mid):
            a = a.next

        return a.data

