from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = set()
        nums += [-1]
        stack = [-1]
        for i, x in enumerate(nums):        
            while x == nums[stack[-1]]:
                stack.pop()
            if x < nums[stack[-1]]:
                pt = i
                while stack and x <= nums[stack[-1]]:
                    t = stack.pop()
                    if stack and x < nums[t] and nums[t] != 0 :
                        ans.add((stack[-1], pt))             
                    pt = t
            stack.append(i)

        return len(ans)

    def minOperations(self, nums: List[int]) -> int:
        st = []
        ans = 0
        for i, x in enumerate(nums):
            while st and x < nums[st[-1]]:
                st.pop()
                ans += 1
            if not st or x != nums[st[-1]]:
                st.append(i)
        return ans + len(st) - (1 if st and st[0] == 0 else 0)
    
t = Solution()
t.minOperations([3,1,2,1])