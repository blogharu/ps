class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i, j = 1, 2
        for _ in range(n-2):
            i, j = j, i + j
        return j
