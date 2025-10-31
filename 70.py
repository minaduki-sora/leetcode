class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 1
        f1 = 1
        f2 = f0 + f1
        for _ in range(n-2):
            f0, f1 = f1, f2
            f2 = f0 + f1
        return f2 if n > 1 else 1
