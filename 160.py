from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tail = headA
        while tail.next:
            tail = tail.next
        tb = headB
        while tb.next:
            tb = tb.next
        if tail != tb:
            return None
        tail.next = headA
        slow = headB
        fast = headB
        while True:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        head = headB
        while head != slow:
            head = head.next
            slow = slow.next
        tail.next = None
        return slow
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p