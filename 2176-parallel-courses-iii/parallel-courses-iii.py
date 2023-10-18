from collections import defaultdict
from heapq import heappush, heappop, heapify

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        a_to_b = defaultdict(set)
        b_to_a = defaultdict(set)

        for (a, b) in relations:
            a_to_b[a-1].add(b-1)
            b_to_a[b-1].add(a-1)
        
        nodes = [(time[i], i) for i in range(n) if len(b_to_a[i]) == 0]
        heapify(nodes)
        answer = 0
        while nodes:
            answer, i = heappop(nodes)
            for b in a_to_b[i]:
                b_to_a[b].remove(i)
                if len(b_to_a[b]) == 0:
                    heappush(nodes, (answer + time[b], b))
        return answer