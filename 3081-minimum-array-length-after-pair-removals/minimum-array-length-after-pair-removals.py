from collections import Counter
from heapq import heappush, heappop

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        heap = []
        nums = Counter(nums)
        for num, count in nums.items():
            heappush(heap, (-count, num))
        while len(heap) > 1:
            for count, num in [heappop(heap), heappop(heap)]:
                count *= -1 
                if count > 1:
                    heappush(heap, (-(count-1), num))
        return 0 if len(heap) == 0 else -heap[0][0]
        
        