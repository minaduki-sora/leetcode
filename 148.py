from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = None
        fast = head
        while fast and fast.next:
            slow = slow.next if slow else head
            fast = fast.next.next
        p = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(p)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        p.next = list1 if list1 else list2
        return dummy.next