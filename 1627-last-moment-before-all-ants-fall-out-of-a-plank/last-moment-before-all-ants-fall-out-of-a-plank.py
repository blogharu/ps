class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        answer = -1
        for l in left:
            answer = max(answer, l)
        for r in right:
            answer = max(answer, n - r)
        return answer