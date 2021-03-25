class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        A1=ListNode(1)
        A1.next=A
        front=A.next
        middle=A
        back=A1
        f=0
        while front:
            if front.val==middle.val:
                front=front.next
                f=1
            else:
                if f==0:
                    back=back.next
                    middle=middle.next
                    front=front.next
                else:
                    back.next=front
                    middle=front
                    front=front.next
                    f=0
                
        if f>0:
            back.next=None
        return A1.next