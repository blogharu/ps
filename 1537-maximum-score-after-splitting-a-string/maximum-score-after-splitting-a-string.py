class Solution:
    def maxScore(self, s: str) -> int:
        answer = 0
        for i in range(1, len(s)):
            answer = max(answer, s[:i].count("0") + s[i:].count("1"))
        return answer
        