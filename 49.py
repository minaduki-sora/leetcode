from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = dict()
        for s in strs:
            c = tuple(sorted(s))
            if cnt.get(c):
                cnt[c].append(s)
            else:
                cnt[c] = [s]
        ans = [x for x in cnt.values()]
        return ans

t = Solution()
t.groupAnagrams(["eat","tea","tan","ate","nat","bat"])