from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = -1001
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal maxsum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maxsum = max(maxsum, root.val, root.val + left + right, root.val + left, root.val + right)
            return max(root.val + left, root.val + right, 0)

        return maxsum

n1 = TreeNode(1, TreeNode(2), TreeNode(3))
t = Solution()
t.maxPathSum(n1)