from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = None
        p = head
        while p.next:
            q = p.next
            p.next = prev
            prev = p
            p = q
        p.next = prev
        return p