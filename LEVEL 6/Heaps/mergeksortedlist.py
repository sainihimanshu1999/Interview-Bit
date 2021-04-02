def mergeKLists(self, A):
    heap = []
    for i in range(len(A)):
        heappush(heap,(A[i].val,A[i].next))
    pop_val,pop_next = heappop(heap)
    head = prev = ListNode(pop_val)
    if pop_next:
        heappush(heap,(pop_next.val,pop_next.next))
    while len(heap)>0:
        pop_val,pop_next = heappop(heap)
        if pop_next:
            heappush(heap,(pop_next.val,pop_next.next))
        new_node = ListNode(pop_val)
        prev.next = new_node
        prev = new_node
    return head