from heapq import heappush, heappop

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        answer = max(nums)
        heap = [(0, -1)]
        for i in range(len(nums)-1, -1, -1):
            while heap[0][1] > i+k:
                heappop(heap)
            if (temp := nums[i] + -heap[0][0]) > 0:
                heappush(heap, (-temp, i))
                answer = max(answer, temp)
        return answer     