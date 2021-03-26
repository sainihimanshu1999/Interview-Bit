# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        length = 0
        curr = A
        res = A
        while curr:
            curr= curr.next
            length+=1
        k = B%length
        if k==0:
            return A
        
        front = A
        back = A
        
        while front.next and k>0:
            front=front.next
            k-=1
        
        while back.next and front.next:
            front = front.next
            back = back.next
            
            
        res = back.next
        back.next = None
        front.next = A
        
        return res
            
