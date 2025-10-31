from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        ans.append(l if 0 <= l <= len(nums) - 1 and nums[l] == target else -1)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        ans.append(r if 0 <= r <= len(nums) - 1 and nums[r] == target else -1)
        return ans

t = Solution()
t.searchRange([5,7,7,8,8,10], 6)