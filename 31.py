from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            minmax = 101
            mmp = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and nums[j] <= minmax:
                    minmax = nums[j]
                    mmp = j
            nums[i], nums[mmp] = nums[mmp], nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

a = Solution()
a.nextPermutation([1,2,3])
        
        