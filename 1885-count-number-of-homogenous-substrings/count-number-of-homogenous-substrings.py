MOD = 1000000007

class Solution:
    def countHomogenous(self, s: str) -> int:
        answer = 0
        prev = ''
        count = 0
        cache = {}
        for c in s:
            if c != prev:
                if count not in cache:
                    cache[count] = count * (count+1) // 2
                answer = (answer + cache[count]) % MOD
                prev = c
                count = 1
            else:
                count += 1
        return (answer + count * (count+1) // 2) % MOD