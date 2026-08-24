# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        dummy = ListNode()
        tail = dummy
        tie = 0
        for h in lists:
            if h:
                heapq.heappush(min_heap,(h.val,tie,h))
                tie += 1
        
        while min_heap:
            m = heapq.heappop(min_heap)
            min_node = m[2]
            nxt = min_node.next
            tail.next = min_node
            tail = tail.next
            if nxt:
                heapq.heappush(min_heap,(nxt.val,tie,nxt))
                tie += 1




        return dummy.next