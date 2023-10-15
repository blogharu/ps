from functools import cache

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def getAnswer(i, step):
            if step == 0 or i < 0:
                return 1 if i == 0 else 0
            answer = getAnswer(i, step-1)
            if i > 0:
                answer += getAnswer(i-1, step-1)
            if i < arrLen-1:
                answer += getAnswer(i+1, step-1)
            return answer % 1000000007
        return getAnswer(0, steps)
        