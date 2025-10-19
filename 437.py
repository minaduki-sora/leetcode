from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root: Optional[TreeNode], prefixSum: int):
            nonlocal cnt
            prefixSum += root.val
            # 枚举右端点，利用前缀和计算子路径和
            cnt += sumdict[prefixSum - targetSum]
            sumdict[prefixSum] += 1
            if root.left:
                dfs(root.left, prefixSum)
            if root.right:
                dfs(root.right, prefixSum)
            # 回溯
            sumdict[prefixSum] += 1

        cnt = 0
        sumdict = defaultdict(int)
        if not root:
            return 0
        sumdict[0] += 1
        dfs(root, 0)
        return  cnt