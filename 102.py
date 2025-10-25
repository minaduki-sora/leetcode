from typing import Optional, List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depthdict = defaultdict(list)
        maxd = 0
        def dfs(root: Optional[TreeNode], d: int):
            if not root:
                return
            nonlocal maxd
            maxd = max(maxd, d)
            depthdict[d].append(root.val)
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        dfs(root, 0)
        ans = [depthdict[i] for i in range(maxd+1)]
        return ans
        