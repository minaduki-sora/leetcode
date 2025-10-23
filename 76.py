from collections import Counter

class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     cnt_t = Counter(t)
    #     cnt_s = Counter()
    #     ans = s + "1"
    #     left = 0
    #     for right, x in enumerate(s):
    #         if x in cnt_t:
    #             cnt_s[x] += 1
    #         if cnt_s >= cnt_t:
    #             while cnt_s >= cnt_t:
    #                 out = s[left]
    #                 if out in cnt_t:
    #                     cnt_s[out] -= 1
    #                 left += 1
    #                 if len(ans) > right - left + 1:
    #                     ans = s[left-1:right+1]
    #     return ans if len(ans) <= len(s) else ""

    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        ans_left = 0
        ans_right = len(s) + 1
        less = len(cnt_t.keys())

        left = 0
        for right, x in enumerate(s):
            if x in cnt_t:
                cnt_t[x] -= 1
                if cnt_t[x] == 0:
                    less -= 1
            while less <= 0:
                out = s[left]
                if out in cnt_t:
                    cnt_t[out] += 1
                    if cnt_t[out] == 1:
                        less += 1
                left += 1
                if ans_right - ans_left > right - left + 1:
                    ans_right = right
                    ans_left = left - 1
        return "" if ans_right == len(s) + 1 else s[ans_left:ans_right+1]

t = Solution()
t.minWindow("ADOBECODEBANC", "ABC")