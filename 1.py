from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, x in enumerate(nums):
            if target - x in hashtable:
                return [hashtable[target - x], i]
            hashtable[x] = i