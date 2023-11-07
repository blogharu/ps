from heapq import heappush, heappop

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for d, s in zip(dist, speed):
            heappush(heap, d // s + (d % s > 0))
        answer = 0
        for t in range(len(dist)):
            if heap[0] <= t:
                break
            heappop(heap)
            answer += 1
        return answer

        