from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            p.next = ListNode(s%10)
            p = p.next
            c = s // 10
            l1, l2 = l1.next, l2.next
        while l1:
            s = l1.val + c
            p.next = ListNode(s%10)
            p = p.next
            c = s // 10
            l1= l1.next
        while l2:
            s = l2.val + c
            p.next = ListNode(s%10)
            p = p.next
            c = s // 10
            l2= l2.next
        if c:
            p.next = ListNode(c)
        return dummy.next