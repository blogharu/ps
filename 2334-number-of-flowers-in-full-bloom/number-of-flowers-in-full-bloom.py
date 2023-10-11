from collections import deque
from heapq import heappush, heappop

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people_dict = {p:0 for p in people}
        people_keys = sorted(people_dict.keys())
        flowers = deque(sorted((start, end) for (start, end) in flowers))
        heap = []
        for p in people_keys:
            while heap and heap[0] < p:
                heappop(heap)
            while flowers:
                if flowers[0][0] > p:
                    break
                elif flowers[0][1] < p:
                    flowers.popleft()
                else:
                    heappush(heap, flowers.popleft()[1])
            people_dict[p] = len(heap)            
        return [people_dict[p] for p in people]
        