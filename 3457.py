from typing import List
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas = sorted(pizzas)
        s = 0
        end = n - 1
        if n % 8:
            s += pizzas[end]
            end -= 1
        for _ in range(n//8):
            s += pizzas[end]
            end -= 1
        for _ in range(n//8):
            s += pizzas[end -2]
            end -= 2
        
        return s