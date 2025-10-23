from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_w = Counter()
        cnt_p = Counter(p)
        ans = []
        for i, x in enumerate(s):
            cnt_w[x] += 1
            left = i - len(p) + 1
            if left < 0:
                continue
            if cnt_p == cnt_w:
                ans.append(left)
            out = s[left]
            cnt_w[out] -= 1
            if cnt_w[out] == 0:
                del cnt_w[out]
        return ans
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        ans = []
        left = 0
        for right, x in enumerate(s):
            cnt[x] -= 1
            while cnt[x] < 0:
                cnt[s[left]] += 1
                left += 1
            if right == left + len(p) - 1:
                ans.append(left)
        return ans

t = Solution()
t.findAnagrams("cbaebabacd", "abc")