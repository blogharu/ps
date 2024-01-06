from collections import defaultdict
from bisect import bisect_left
from functools import cache

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = defaultdict(list)
        for start, end, value in zip(startTime, endTime, profit):
            jobs[start].append((end,value))
        starts = sorted(jobs.keys())
        @cache
        def get_answer(i):
            if i == len(starts):
                return 0
            start = starts[i]
            answer = get_answer(i+1)
            for end, value in jobs[start]:
                answer = max(answer, get_answer(bisect_left(starts, end, lo=i+1)) + value)
            return answer
        return get_answer(0)
