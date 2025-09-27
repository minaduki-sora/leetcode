class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(lettertable: dict):
            for i in lettertable.values:
                if i < 0:
                    return False
            return True
        
        lettertable = dict()
        for i in t:
            if i in lettertable:
                lettertable[i] -= 1
            else:
                lettertable[i] = -1
        
        start = 0
        end = 0
        records = ""
        flag = True
        for i, x in enumerate(s):
            if x in lettertable:
                start = i
                lettertable[x] += 1
                flag = False
                break
        if flag:
            return ""
        
        sl = len(s)
        end = start + 1
        while end < sl:
            if s[end] in lettertable:
                lettertable[s[end]] += 1
            end += 1
            if check(lettertable):
                record = s[start:end] if end - start < len(record) else record
                lettertable[s[start]] -= 1
                start += 1
                while check(lettertable):
                    if s[start] in lettertable:
                        lettertable[s[start]] -= 1
                    start += 1


            
