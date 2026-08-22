# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None # Crucial step to avoid cycles

        prev = None
        while mid:
            m = mid.next
            mid.next = prev
            prev = mid
            mid = m
        left = head
        right = prev

        while left and right:
            l = left.next
            left.next = right
            left = l

            r = right.next
            right.next = left
            right = r
        
