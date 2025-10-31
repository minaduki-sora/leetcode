from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def isblue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target <= nums[i] and target > end
            return target <= nums[i] or target > end

        left, right = 0, len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if isblue(mid):
                right = mid - 1
            else:
                left = mid + 1
        return -1 if left == len(nums) else left