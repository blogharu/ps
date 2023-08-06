from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ms = defaultdict(list)

        for v, m in zip(nums1, nums2):
            ms[m].append(v)
        
        heap = []
        answer = 0
        s = 0

        for m in sorted(ms.keys(), reverse=True):
            for val in ms[m]:
                heappush(heap, val)
                s += val
                if len(heap) > k:                    
                    s -= heappop(heap)
            if len(heap) == k:
                answer = max(answer, s * m)

        return answer
