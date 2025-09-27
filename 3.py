# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxlen = 0
#         for i in range(0, len(s)):
#             cset = set()
#             mlen = 0
#             for j in range(i, len(s)):
#                 if s[j] in cset:
#                     break
#                 else:
#                     cset.add(s[j])
#                     mlen += 1
#             maxlen = max(maxlen, mlen)
#         return maxlen

# class Solution:
def lengthOfLongestSubstring(s: str) -> int:
    cdict = dict()
    start = 0
    maxlen = 0
    for i, x in enumerate(s):
        if x in cdict:
            start = cdict.pop(x) + 1
        cdict[x] = i
        maxlen = max(maxlen, i - start + 1)
    return maxlen

s = "abcabcbb"

lengthOfLongestSubstring(s)