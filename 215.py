from typing import List
from random import randint

class Solution:
    def partition(self, nums: List[int], left: int, right: int):
        i = randint(left, right)
        pivot = nums[i]
        nums[left], nums[i] = nums[i], nums[left]

        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j


    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while True:
            j = self.partition(nums, left, right)
            if j == n - k:
                return nums[j]
            elif j > n - k:
                right = j - 1
            else:
                left = j + 1