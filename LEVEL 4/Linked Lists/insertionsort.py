# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        stack  = []
        temp = A
        while temp:
            stack.append(temp.val)
            temp = temp.next
        stack.sort()
        temp = A
        while stack:
            temp.val = stack.pop(0)
            temp = temp.next
        return A
    
                
                