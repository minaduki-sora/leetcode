from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count = 0
        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1
        
        dummy = ListNode()
        curr = dummy
        
        while heap:
            val, _, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
        
        return dummy.next
    
    def merge_two_lists(self, list1, list2):
        dummy = ListNode()
        dptr = dummy
        if not list1 or not list2:
            return list1 if list1 else list2
        ptr1, ptr2 = list1, list2
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                dptr.next = ptr1
                ptr1 = ptr1.next
                dptr = dptr.next
            else:
                dptr.next = ptr2
                ptr2 = ptr2.next
                dptr = dptr.next
        dptr = ptr1 if ptr1 else ptr2
        return dummy.next
    
    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l + r) // 2
        return self.merge_two_lists(self.merge(lists, l, mid), self.merge(lists, mid+1, r))
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists)-1)
        