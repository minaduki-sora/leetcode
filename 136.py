from typing import List
from random import randint

class Solution:
    def partition(self, nums: List[int], left: int, right: int):
        i = randint(left, right)
        pivot = nums[i]
        nums[left], nums[i] = nums[i], nums[left]

        # 三路划分：小于pivot | 等于pivot | 大于pivot
        lt = left      # 小于pivot的右边界
        gt = right     # 大于pivot的左边界
        i = left + 1   # 当前检查的位置
        
        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:  # nums[i] == pivot
                i += 1
        
        return lt, gt
        
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while True:
            lt, gt = self.partition(nums, left, right)
            if lt == gt:
                return nums[lt]
            if (lt - left) % 2:
                right = lt - 1
            else:
                left = gt + 1

            
