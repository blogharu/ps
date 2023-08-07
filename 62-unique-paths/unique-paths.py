from math import comb

MOD = 2 * 10**9

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2,n-1) % MOD