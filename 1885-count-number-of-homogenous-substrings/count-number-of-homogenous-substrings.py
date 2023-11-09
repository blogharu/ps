MOD = 1000000007

class Solution:
    def countHomogenous(self, s: str) -> int:
        answer = 0
        prev = ''
        count = 0
        for c in s:
            if c != prev:
                answer = (answer + count * (count+1) // 2) % MOD
                prev = c
                count = 1
            else:
                count += 1
        return (answer + count * (count+1) // 2) % MOD