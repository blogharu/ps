from functools import cache
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 0

        ps = defaultdict(set)
        ys = defaultdict(int)

        for (x, y) in points:
            ps[x].add(y)
            ys[y] += 1
            answer = max(answer, len(ps[x]), ys[y])
        
        @cache
        def get_answer(m, y):
            answer = 0
            for x in ps:
                xx = m*x + y
                rxx = round(xx)
                if abs(xx - rxx) < 0.0001:
                    answer += rxx in ps[x]
            return answer

        xs = list(ps.keys())

        for i, x in enumerate(xs):
            for y in ps[x]:
                for j in range(i+1, len(xs)):
                    x2 = xs[j]
                    for y2 in ps[x2]:
                        m = (y-y2)/(x-x2)
                        answer = max(answer, get_answer(m, y-m*x))

        return answer