from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root: Optional[TreeNode], tail: TreeNode):
            if not root:
                return tail
            if tail:
                tail.right = root
                tail.left = None
            rightp = root.right
            tail = root
            tail = dfs(root.left, tail)
            tail = dfs(rightp, tail)
            return tail
        dfs(root, None)
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        root.right = self.head
        root.left = None
        self.head = root
