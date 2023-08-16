from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]
        answer = []
        heap = []
        for i in range(k-1):
            heappush(heap, (-nums[i], i))
        for i, num in enumerate(nums[k-1:], k-1):
            heappush(heap, (-num, i))
            while heap[0][1] <= i - k:
                heappop(heap)
            answer.append(-heap[0][0])
        return answer