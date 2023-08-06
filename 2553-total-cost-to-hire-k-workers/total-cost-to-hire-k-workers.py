from heapq import heappush, heappop
from collections import deque

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) == k:
            return sum(costs)

        answer = 0
        costs = deque(costs)
        heapl, heapr = [], []

        for _ in range(candidates):
            if len(costs) > 1:
                heappush(heapl, costs.popleft())
                heappush(heapr, costs.pop())
            elif costs:
                heappush(heapl, costs.popleft())
        
        for _ in range(k):
            if costs and heapl[0] == heapr[0]:
                is_left = costs[0] <= costs[-1]
            else:
                is_left =  heapl[0] < heapr[0]
            if is_left:
                answer += heappop(heapl)
                heappush(heapl, costs.popleft() if costs else 10**6)
            else:
                answer += heappop(heapr)
                heappush(heapr, costs.pop() if costs else 10**6)
            k -= 1
        
        return answer