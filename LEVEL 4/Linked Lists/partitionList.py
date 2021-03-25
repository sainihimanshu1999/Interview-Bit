# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        smallerHead = None
        smallerLast = None
        greaterLast = None
        greaterHead = None
        equalHead = None
        equalLast = None
        
        while(A!=None):
            if(A.val == B):
                if(equalHead == None):
                    equalHead = equalLast = A
                else:
                    equalLast.next = A
                    equalLast = equalLast.next
            elif(A.val <B):
                if smallerHead == None:
                    smallerHead = smallerLast = A
                else:
                    smallerLast.next = A
                    smallerLast = A
            else:
                if greaterHead == None:
                    greaterHead = greaterLast = A
                else:
                    greaterLast.next = A
                    greaterLast = A
            A = A.next
            
        if greaterHead != None:
            greaterLast.next = None
        
        if smallerHead == None:
            if equalHead == None:
                return greaterHead
            equalLast.next = greaterHead
            return equalHead
        
        if equalHead == None:
            smallerLast.next =  greaterHead
            return smallerHead
            
        smallerLast.next = equalHead
        equalLast.next = greaterHead
        return smallerHead
