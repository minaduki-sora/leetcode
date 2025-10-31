from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha = {c: i for i, c in enumerate(s)}
        
        left = 0
        d = 0
        ans = []
        for i, x in enumerate(s):
            d = max(d, alpha[x])
            if d == i:
                ans.append(i - left + 1)
                left = i + 1
        return ans