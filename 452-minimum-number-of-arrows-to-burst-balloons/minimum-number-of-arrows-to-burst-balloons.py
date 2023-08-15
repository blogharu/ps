class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        answer = 0
        min_end = -2**32
        for end, start in sorted([(y, x) for x, y in points]):
            if start > min_end:
                answer += 1
                min_end = end
        return answer