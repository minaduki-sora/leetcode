from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        cnt = dict()
        maxd = 0
        def dfs(root: Optional[TreeNode], d: int):
            if not root:
                return
            nonlocal maxd
            maxd = max(maxd, d)
            cnt[d] = root.val
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        dfs(root, 0, 0)
        ans = [cnt[i] for i in range(maxd+1)] if cnt else []
        return ans

sol = Solution()
sol.rightSideView()