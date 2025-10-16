from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseKNodes(h, t):
            "K nodes including h-t"
            if h == t:
                return h
            a = h
            b = h.next
            h.next = t.next
            while b != t:
                c = b.next
                b.next = a
                a, b = b, c
            b.next = a
            return t
        def nextKnodes(h, K):
            "next k nodes not including h"
            cur = h
            cnt = 0
            while cur.next and cnt < K:
                cnt += 1
                cur = cur.next
            return cur if cnt == K else None
        dummy = ListNode()
        dummy.next = head
        h = dummy
        cur = nextKnodes(h, k)
        while cur:
            temp = h.next
            h.next = reverseKNodes(h.next, cur)
            h = temp
            cur = nextKnodes(h, k)
        return dummy.next
            
