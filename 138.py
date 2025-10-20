from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodedict = dict()
        dummy = Node(0)
        prev = dummy
        p = head
        while p:
            q = Node(p.val)
            prev.next = q
            prev = prev.next
            nodedict[p] = q
            p = p.next
        p = head
        while p:
            nodedict[p].random = nodedict[p.random] if p.random else None
            p = p.next

        return dummy.next
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        while p:
            q = Node(p.val, p.next)
            p.next = q
            p = q.next
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        p = head
        dummy = Node(0)
        prev = dummy
        while p:
            prev.next = p.next
            prev = p.next
            p.next = prev.next
            p = p.next
        return dummy.next
