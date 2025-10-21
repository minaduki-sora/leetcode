from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn = set(nums)
        cnt = defaultdict(int)
        maxlen = 0
        def search(x: int):
            nonlocal maxlen
            t = x
            while t in sn:
                if cnt[t]:
                    cnt[x] += cnt[t]
                    break
                else:
                    if t != x:
                        cnt[t] += 1 # visited
                    cnt[x] += 1
                    t += 1
            maxlen = max(maxlen, cnt[x])

        for x in sn:
            if cnt[x] == 0:
                search(x)
        return maxlen
    
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = set(nums)
        maxlen = 0
        for x in cnt:
            if x - 1 in cnt:
                continue

            y = 0
            while x + y in cnt:
                y += 1
            maxlen = max(maxlen, y)
        return maxlen


