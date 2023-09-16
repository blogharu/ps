class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return max(min(2**31-1, int(str(dividend/divisor).split(".")[0])), -2**31)