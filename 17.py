from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        dmap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        for s in digits:
            ss = dmap.get(s)
            if len(ans) == 0:
                for i in ss:
                    ans.append(i)
            else:
                ans1 = []
                for prefix in ans:
                    for i in ss:
                        ans1.append(prefix+i)
                ans = ans1
        return ans