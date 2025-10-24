from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(row: List[int], target: int) -> bool:
            left = 0
            right = len(row) - 1
            if target < row[left] or target > row[right]:
                return False
            while left <= right:
                mid = (left + right) // 2
                if target == row[mid]:
                    return True
                elif target < row[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for row in matrix:
            if binarysearch(row, target):
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False

    
t = Solution()
t.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)