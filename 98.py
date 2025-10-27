from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root: Optional[TreeNode]):
            if not root:
                return True, None, None
            fl, lm, li = bst(root.left)
            if not fl:
                return False, None, None
            if lm is not None and lm >= root.val:
                return False, None, None
            fr, rm, ri = bst(root.right)
            if not fr:
                return False, None, None
            if ri is not None and ri <= root.val:
                return False, None, None
            return True, rm if rm else root.val, li if li else root.val
        
        flag, _, _ = bst(root)
        return flag