from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        if n == 1:
            return True

        p = head
        prev = None
        for _ in range(n//2):
            pnext = p.next
            p.next = prev
            prev = p
            p = pnext
        left = prev
        right = p.next if n & 1 else p
        for _ in range(n//2):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


