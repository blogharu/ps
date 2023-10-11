# 9:32
# 

from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        heap = []
        for i in range(k):
            heappush(heap, (-nums[i], i))
        answer.append(-heap[0][0])
        for i, num in enumerate(nums[k:]):
            while heap and heap[0][1] <= i:
                heappop(heap)
            heappush(heap, (-num, i+k))
            answer.append(-heap[0][0])

        return answer