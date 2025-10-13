from typing import List
import numpy as np

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        map = np.zeros(20001, dtype=int)
        maxl = 0
        for s in intervals:
            map[2*s[0]:2*s[1]+1] = 1
            maxl = max(maxl, s[1])
        merged_intervals = []
        i = right = 0
        while i <= 2*maxl:
            if map[i] == 1:
                for j in range(i, 2*maxl+1):
                    if map[j] == 1:
                        right = j
                    else:
                        break
                merged_intervals.append([i/2,right/2])
                i = right + 1
            else:
                i += 1
        return merged_intervals
                
        
        