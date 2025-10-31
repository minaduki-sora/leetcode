from typing import List
from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            a, b = nums2, nums1
        else:
            a, b = nums1, nums2
        
        m, n = len(a), len(b)
        
        left, right = -1, len(a)
        while left + 1 < right:
            i = (left + right) // 2
            j = (m + n - 1) // 2 - i - 1
            if a[i] <= b[j + 1]:
                left = i
            else:
                right = i
        i = left
        j = (m + n - 1) // 2 - i - 1
        ai = a[i] if i >= 0 else -inf
        bj = b[j] if j >= 0 else -inf
        ai1 = a[i+1] if i + 1 < m else inf
        bj1 = b[j+1] if j + 1 < n else inf
        max1 = max(ai, bj)
        min2 = min(ai1, bj1)
        return max1 if (m+n)%2 else (max1+min2)/2     
