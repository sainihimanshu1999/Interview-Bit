# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A==None:
            return None
        temp =  A
        new = None
        prev = None
        count = 0
        
        while temp is not None and count <2:
            new = temp.next
            temp.next = prev
            prev =temp
            temp = new
            count += 1
        if new is not None:
            A.next = self.swapPairs(new)
        
        return prev
