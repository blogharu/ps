from heapq import heappush, heappop

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people_dict = {p:0 for p in people}
        people_keys = sorted(people_dict.keys())
        flowers = sorted((start, end) for (start, end) in flowers)
        f = 0
        heap = []
        for p in people_keys:
            while heap and heap[0] < p:
                heappop(heap)
            while f < len(flowers) and flowers[f][0] <= p:
                if flowers[f][1] >= p:
                    heappush(heap, flowers[f][1])
                f += 1
            people_dict[p] = len(heap)            
        return [people_dict[p] for p in people]
        