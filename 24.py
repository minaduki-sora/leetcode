from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        p = head
        prev = dummy
        while p and p.next:
            q = p.next
            p.next = q.next
            q.next = p
            prev.next = q
            prev = p
            p = p.next
        return dummy.next
            