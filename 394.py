class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        ans = []
        left = 0
        while left < n:
            if s[left].isdigit():
                right = left + 1
                while s[right].isdigit():
                    right += 1
                num = int(s[left:right])
                st = ['[']
                end = right + 1
                while st:
                    if s[end] == '[':
                        st.append('[')
                    elif s[end] == ']':
                        st.pop()
                    end += 1
                ans.append(self.decodeString(s[right+1:end-1]) * num)
                left = end
            else:
                ans.append(s[left])
                left += 1
        return "".join(ans)
                
                