from collections import defaultdict, deque

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._lru_cache = {}
        self._counter = defaultdict(int)
        self._history = deque()

    def get(self, key: int) -> int:
        result = -1
        if key in self._lru_cache:
            result = self._lru_cache[key]
            self._update(key)
        return result

    def put(self, key: int, value: int) -> None:
        self._lru_cache[key] = value
        self._update(key)
    
    def _update(self, key) -> None:
        self._counter[key] += 1
        self._history.append(key)
        while len(self._counter) > self._capacity:
            val = self._history.popleft()
            self._counter[val] -= 1
            if self._counter[val] == 0:
                del self._counter[val]
                del self._lru_cache[val]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)