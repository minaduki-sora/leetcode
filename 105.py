from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        ri = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:ri+1], inorder[:ri])
        right = self.buildTree(preorder[ri+1:], inorder[ri+1:])
        return TreeNode(preorder[0], left, right)