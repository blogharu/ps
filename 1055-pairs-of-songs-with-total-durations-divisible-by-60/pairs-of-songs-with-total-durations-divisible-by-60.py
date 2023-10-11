from collections import Counter
from math import comb

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        time = Counter(t % 60 for t in time)
        keys = list(time.keys())
        for i in range(len(keys)):
            a = keys[i]
            if a in {30, 0} and time[a] > 1:
                answer += comb(time[a], 2)
            for j in range(i+1, len(keys)):
                b = keys[j]
                if (a + b) % 60 == 0:
                    answer += time[a] * time[b]
        return answer
        