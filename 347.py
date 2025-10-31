from typing import List
from collections import Counter

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     cnt = Counter(nums)
    #     return [x[0] for x in cnt.most_common(k)]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())

        buckets = [[] for _ in range(max_cnt+1)]
        for x, v in cnt.items():
            buckets[v].append(x)
        
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans
    
t = Solution()
t.topKFrequent([1,1,1,2,2,3], 2)