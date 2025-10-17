from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def susume(x: int, y: int, direction: int):
            m, n = len(matrix), len(matrix[0])
            for _ in range(2):
                if direction == 0 and y+1 < n and matrix[x][y+1] != 1000:
                    return x, y+1, direction
                elif direction == 1 and x+1 < m and matrix[x+1][y] != 1000:
                    return x+1, y, direction
                elif direction == 2 and y-1 >= 0 and matrix[x][y-1] != 1000:
                    return x, y-1, direction
                elif direction == 3 and x-1 >= 0 and matrix[x-1][y] != 1000:
                    return x-1, y, direction
                else:
                    direction += 1
                    direction %= 4
            return 0, 0, 0
        direction = 0
        x, y = 0, 0
        ans = []
        while matrix[x][y] != 1000:
            ans.append(matrix[x][y])
            matrix[x][y] = 1000
            x, y, direction = susume(x, y, direction)
        return ans

sol = Solution()
sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])