from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0, 0
            l1, l2 = dfs(root.left)
            r1, r2 = dfs(root.right)
            return max(l1, r1) + 1, max(l2, r2, l1 + r1)
        l1, l2 = dfs(root)
        return max(l1 - 1, l2)
