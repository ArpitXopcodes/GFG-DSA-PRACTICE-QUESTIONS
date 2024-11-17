'''remove duplicates from sorted array or list 
first made a linked list where curr = current node to go through the list 1 - 1
loop will run till the end of the list...
and if the current data will be equal to 
the next data the in will ignore that element
and go to the next element not returning the prev element... 
else it will go forward after returning it to the element '''

def removeDuplicates(head):
    #code here
    curr = head
    elements = []
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
           curr = curr.next
    return elements
