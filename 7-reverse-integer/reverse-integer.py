class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x >= 0 else int(f"-{int(str(-x)[::-1])}")
        return result if -2**31 <= result <= 2**31 - 1 else 0