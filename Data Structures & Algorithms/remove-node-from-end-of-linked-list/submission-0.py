class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        k = 0

        while r and k < n:
            r = r.next
            k += 1

        while r:
            l = l.next
            r = r.next

        nxt = l.next
        l.next = l.next.next
        nxt.next = None

        return dummy.next
