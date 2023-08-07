class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a, b, c = 0, 1, 1
        while n > 2:
            a, b, c, n = b, c, a+b+c, n-1
        return c
        