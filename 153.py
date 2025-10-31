from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid
            else:
                right = mid
        return nums[right]