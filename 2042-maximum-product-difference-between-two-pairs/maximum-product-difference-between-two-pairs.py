from heapq import heappush, heappop

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxs = []
        mins = []
        for num in nums:
            heappush(maxs, num)
            heappush(mins, -num)
            if len(maxs) > 2:
                heappop(maxs)
                heappop(mins)
        return maxs[0] * maxs[1] - mins[0] * mins[1]
