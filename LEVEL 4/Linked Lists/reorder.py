# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        temp = A
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
            
        temp = A
        i = 0
        n = len(stack)
        while i<(n//2+1) and temp:
            temp.val = stack[i]
            temp = temp.next
            
            if (n-i-1)!=i:
                temp.val = stack[n-i-1]
                temp = temp.next
            i+=1
        return A
            
