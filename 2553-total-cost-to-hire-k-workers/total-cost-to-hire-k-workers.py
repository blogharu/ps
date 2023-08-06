from heapq import heappush, heappop
from collections import deque

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        answer = 0
        costs = deque(costs)
        heapl, heapr = [], []

        for _ in range(candidates):
            if len(costs) > 1:
                heappush(heapl, costs.popleft())
                heappush(heapr, costs.pop())
            elif costs:
                heappush(heapl, costs.popleft())
        
        while k and costs:
            if heapl[0] == heapr[0]:
                is_left = costs[0] <= costs[-1]
            else:
                is_left =  heapl[0] < heapr[0]
            if is_left:
                answer += heappop(heapl)
                heappush(heapl, costs.popleft())
            else:
                answer += heappop(heapr)
                heappush(heapr, costs.pop())
            k -= 1
        
        while k and heapl and heapr:
            if heapl[0] <= heapr[0]:
                answer += heappop(heapl)
            else:
                answer += heappop(heapr)
            k -= 1

        heap = heapl if heapl else heapr
        for _ in range(k):
            answer += heappop(heap)

        return answer