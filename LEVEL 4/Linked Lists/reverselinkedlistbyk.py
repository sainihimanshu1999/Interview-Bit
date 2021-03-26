# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        temp = A
        while temp:
            stack = []
            t1 = temp
            i = B
            while i>0 and temp:
                stack.append(temp.val)
                temp = temp.next
                i-=1
            i = B-1
            while(i>-1) and t1:
                t1.val = stack[i]
                t1 = t1.next
                i-=1
            temp = t1
        return A
