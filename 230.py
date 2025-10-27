from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            nonlocal cnt, ans
            dfs(root.left)
            cnt += 1
            if cnt == k:
                ans = root.val
            dfs(root.right)
        dfs(root)
        return ans