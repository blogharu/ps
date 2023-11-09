from collections import defaultdict

MOD = 1000000007

class Solution:
    def countHomogenous(self, s: str) -> int:
        counts = defaultdict(int)
        prev = ''
        count = 0
        for c in s:
            if c != prev:
                counts[count] += 1
                prev = c
                count = 1
            else:
                count += 1
        counts[count] += 1
        answer = 0
        for count, val in counts.items():
            answer = (answer + (val * count * (count+1) // 2)) % MOD
        return answer