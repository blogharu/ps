class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        while a or b or c:
            if c % 2 == 0:
                answer += (a % 2) + (b % 2)
            elif (a % 2) + (b % 2) == 0:
                answer += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return answer