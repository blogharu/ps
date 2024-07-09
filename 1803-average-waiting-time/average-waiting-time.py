class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        acc = 0
        finished_time = -1
        for arrieve, time in customers:
            start = max(arrieve, finished_time)
            finished_time = start + time
            acc += finished_time - arrieve
        return acc / len(customers)
        