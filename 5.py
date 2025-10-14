class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestr = ""
        llen = 0
        slen = len(s)
        for c in range(0, slen):
            for r in range(0, slen):
                if c-r < 0 or c+r+1 > slen:
                    break
                if s[c-r] != s[c+r]:
                    break
                if llen < 2*r+1:
                    llen = 2*r+1
                    longestr = s[c-r:c+r+1]
            for r in range(0, slen):
                if c-r < 0 or c+r+2 > slen:
                    break
                if s[c-r] != s[c+r+1]:
                    break
                if llen < 2*r+2:
                    llen = 2*r+2
                    longestr = s[c-r:c+r+2]
        return longestr
