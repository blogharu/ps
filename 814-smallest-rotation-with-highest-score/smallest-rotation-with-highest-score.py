from heapq import heappush, heappop

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        heap = []
        for i, num in enumerate(nums):
            if num > i:
                heappush(heap, num-i)

        max_score, answer = -len(heap), 0

        for i in range(1, len(nums)):
            heappush(heap, nums[-i]+i)
            while heap and heap[0] == i:
                heappop(heap)
            if -len(heap) > max_score:
                max_score, answer = -len(heap), len(nums) - i    
            elif -len(heap) == max_score:
                answer = min(len(nums) - i, answer)

        return answer