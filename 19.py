from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # def recursive(head: Optional[ListNode], n: int):
        #     if not head:
        #         return 0
        #     p = recursive(head.next, n)
        #     if p == n:
        #         head.next = head.next.next
        #     elif p >= 0:
        #         return p + 1
        #     return -1
        # p = recursive(head, n)
        # return head.next if p != -1 else head
        dummy = ListNode(0, head)
        right = head
        for _ in range(n):
            right = right.next
        left = dummy
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next