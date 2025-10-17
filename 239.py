from typing import List
from collections import defaultdict,deque
import heapq as hq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        ans = []
        h = []
        for x in nums[:k]:
            cnt[x] += 1
            if cnt[x] == 1:
                hq.heappush(h, -x)
        ans.append(-h[0])
        for i in range(n-k):
            cnt[nums[i]] -= 1
            cnt[nums[i+k]] += 1
            if cnt[nums[i+k]] == 1:
                hq.heappush(h, -nums[i+k])
            while cnt[-h[0]] == 0:
                hq.heappop(h)
            ans.append(-h[0])
        return ans
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = [0] * (len(nums) - k + 1) 
        for i, x in enumerate(nums):
            # 1.入队
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            # 2.出队
            left = i - k + 1
            if q[0] < left:
                q.popleft()
            # 3.记录
            if left >= 0:
                ans[left] = nums[q[0]]        
        return ans


sl = Solution()
sl.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)