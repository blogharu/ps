from collections import defaultdict
from heapq import heappush, heappop

class LFUCache:
    def __init__(self, capacity: int):        
        self._capacity = capacity
        self._cache = {}
        self._lfu = defaultdict(int)
        self._lfu_heap = []
        self._count = 0

    def _update(self, key):
        self._lfu[key] += 1
        heappush(self._lfu_heap, (self._lfu[key], self._count, key))
        self._count += 1

    def get(self, key: int) -> int:        
        val = self._cache.get(key, -1)
        if val >= 0:
            self._update(key)
        return self._cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache[key] = value
            self._update(key)
        else:
            if len(self._cache) == self._capacity:
                while self._lfu_heap:
                    f, _, c = heappop(self._lfu_heap)
                    if f == self._lfu[c]:                
                        break
                del self._lfu[c]
                del self._cache[c]
            self._update(key)
            self._cache[key] = value
        