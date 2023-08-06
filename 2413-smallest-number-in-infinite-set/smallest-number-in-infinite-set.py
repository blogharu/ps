from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self._heap = []
        self._set = set()
        self._count = 1
        
    def popSmallest(self) -> int:
        if self._heap and self._heap[0] <= self._count:
            self._count += self._heap[0] == self._count
            self._set.remove(self._heap[0])
            return heappop(self._heap)
        self._count += 1
        return self._count-1
        
    def addBack(self, num: int) -> None:
        if num not in self._set:
            self._set.add(num)
            heappush(self._heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)