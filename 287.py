from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        head = 0
        while head != slow:
            slow = nums[slow]
            head = nums[head]
        return slow