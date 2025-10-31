from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        def pipei(a, b):
            if a == '(':
                return b == ')'
            elif a == '[':
                return b == ']'
            elif a == '{':
                return b == '}'
            return False
        q = []
        for x in s:
            if q and pipei(q[-1], x):
                q.pop()
            else:
                q.append(x)
        return not q

t = Solution()
t.isValid("([}}])")