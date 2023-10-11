from heapq import heappush, heappop
from collections import deque
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings = deque(sorted((i, j, h) for i, j, h in buildings))
        points = set()
        for i, j, h in buildings:
            points.add(i)
            points.add(j)
        points = sorted(points)
        answer = []
        heap = []
        max_h = 0
        for p in points:
            is_updated = False
            while buildings and buildings[0][0] == p:
                i, j, h = buildings.popleft()
                heappush(heap, (-h, j))
                if max_h < h:
                    max_h = h
                    is_updated = True
            while heap and heap[0][1] <= p:
                heappop(heap)
                h = -heap[0][0] if heap else 0
                if h != max_h:
                    max_h = h
                    is_updated = True
            if is_updated:
                answer.append([p, max_h])
        return answer