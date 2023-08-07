MOD = 10**9 + 7
class Solution:
    def numTilings(self, n: int) -> int:
        nums = [3, 1, 2]
        if n <= 2:
            return nums[n]
        for _ in range(n-2):
            nums[1:] = [nums[2], (nums[0] * 2 - nums[1] - nums[2] + 2) % MOD]
            nums[0] += nums[2]
            nums[0] %= MOD
        return nums[2]