from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return 0 <= left < m * n and matrix[left // n][left % n] == target

t = Solution()
t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61)