from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        cache = {}
        intervals = sorted([(start, end) for start, end in intervals], reverse=True)
        answers = [(float('inf'),float('inf'))]
        for query in sorted(queries):
            if query not in cache:
                while answers and answers[0][1] < query:
                    heappop(answers)
                while intervals and intervals[-1][0] <= query:
                    start, end = intervals.pop()
                    if end >= query:
                        answer = end - start + 1
                        heappush(answers, (answer, end))
                cache[query] = answers[0][0] if len(answers) > 1 else -1
        return [cache.get(query, -1) for query in queries]