from collections import defaultdict
from heapq import heappush, heappop

class AllOne:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.dict = defaultdict(int)
        self.max_pop = []
        self.min_pop = []

    def inc(self, key: str) -> None:
        if key in self.dict:
            heappush(self.max_pop, (-self.dict[key], key))
            heappush(self.min_pop, (self.dict[key], key))
        self.dict[key] += 1
        heappush(self.max_heap, (-self.dict[key], key))
        heappush(self.min_heap, (self.dict[key], key))
        
    def dec(self, key: str) -> None:
        heappush(self.max_pop, (-self.dict[key], key))
        heappush(self.min_pop, (self.dict[key], key))
        self.dict[key] -= 1
        if self.dict[key] == 0:
            self.dict.pop(key)
        else:
            heappush(self.max_heap, (-self.dict[key], key))
            heappush(self.min_heap, (self.dict[key], key))
        
    def getMaxKey(self) -> str:
        while self.max_pop:
            if self.max_heap[0] != self.max_pop[0]:
                break
            heappop(self.max_pop)
            heappop(self.max_heap)
        return self.max_heap[0][1] if self.max_heap else ""
        
    def getMinKey(self) -> str:
        while self.min_pop:
            if self.min_heap[0] != self.min_pop[0]:
                break
            heappop(self.min_pop)
            heappop(self.min_heap)
        return self.min_heap[0][1] if self.max_heap else ""
