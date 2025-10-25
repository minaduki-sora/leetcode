from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymDouble(r1: Optional[TreeNode], r2: Optional[TreeNode]):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            if r1.val != r2.val:
                return False
            return isSymDouble(r1.left, r2.right) and isSymDouble(r1.right, r2.left)
        return isSymDouble(root.left, root.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            l = stack.pop()
            r = stack.pop()
            if (not l and r) or (l and not r):
                return False
            if not l and not r:
                continue
            if l.val != r.val:
                return False
            if l and r:
                stack.append(l.left)
                stack.append(r.right)
                stack.append(l.right)
                stack.append(r.left)
        return True