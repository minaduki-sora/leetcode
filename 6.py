class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        ans = [""] * numRows
        for i in range(0, n, 2 *numRows - 2):
            ans[0] += s[i]
            for j in range(1, min(numRows-1, n-i)):
                ans[j] += s[i+j]
                if i+2*numRows-j < n:
                    ans[j] += s[i+2*numRows-j-2]
            if i + numRows - 1 < n:
                ans[numRows-1] += s[i+numRows-1]
        return "".join(ans)

t = Solution()
t.convert("PAYPALISHIRING", 3)