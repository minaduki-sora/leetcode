class Solution:
    def maxOperations(self, s: str) -> int:
        ans = cnt = 0
        for i, x in enumerate(s):
            if x == '1':
                if i > 0 and s[i-1] == '0':
                    ans += cnt
                cnt += 1
        if s and s[-1] == '0':
            ans += cnt
        return ans