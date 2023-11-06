from heapq import heappush, heappop, heapify

class SeatManager:
    def __init__(self, n: int):
        self._reservables = [i for i in range(1, n+1)]
        heapify(self._reservables)

    def reserve(self) -> int:
        return heappop(self._reservables)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self._reservables, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)