# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        stack = []
        temp= A
        isPalin = 1
        
        while temp!=None:
            stack.append(temp.val)
            temp = temp.next
            
        while A!= None:
            i = stack.pop()
            
            if A.val == i:
                isPalin = 1
            else:
                isPalin = 0
                break
            A = A.next
        return isPalin
