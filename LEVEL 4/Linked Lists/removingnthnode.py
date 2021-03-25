# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        temp = A
        count = 1
        while(temp.next):
            count += 1
            temp = temp.next
        count2 = count - B
        
        if B>=count:
            A = A.next
            return A
        else:
            temp2 = A
        
        for i in range(1,count):
            if i == count2:
                temp2.next = temp2.next.next
            else:
                temp2 = temp2.next
        return A
        
            
            
