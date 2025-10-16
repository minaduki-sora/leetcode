from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def makehash(numlists, hashtable:set):
            for l in numlists:
                hashtable.add(tuple(sorted(l)))
        
        def scan(i, v, nums):
            left = 0
            right = len(nums) - 1
            ans = []
            while left < right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue
                if nums[left] + nums[right] < v:
                    left += 1
                elif nums[left] + nums[right] > v:
                    right -= 1
                else:
                    ans.append([nums[left], nums[right], -v])
                    while left < right:
                        if nums[left] == nums[left + 1]:
                            left += 1
                        else:
                            left += 1
                            break
                    while left < right:
                        if nums[right] == nums[right - 1]:
                            right -= 1
                        else:
                            right -= 1
                            break
                    
            return ans
                    

        nums = sorted(nums)
        hashtable = set()
        for i, v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue
            ans = scan(i,-v,nums)
            makehash(ans, hashtable)
        sumlist = [list(x) for x in hashtable]
        return sumlist

sol = Solution()
sol.threeSum([-1,0,1,2,-1,-4])  