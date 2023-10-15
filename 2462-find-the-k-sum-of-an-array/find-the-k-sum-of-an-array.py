from heapq import heappush, heappop

class Solution:
    def kSum(self, num_list: List[int], k: int) -> int:
        maximum = 0
        heap = []
        for num in num_list:
            maximum += num if num > 0 else 0
            heappush(heap, -abs(num))
            if len(heap) > k:
                heappop(heap)
        heap.sort(reverse=True)
        sums = [(-maximum, 0)]        
        done = {sums[0]}
        sums_reverse = [maximum]
        for n in range(k, 1, -1):
            c, c_bit = heappop(sums)
            for i, val in enumerate(heap):
                i_bit = 1 << i
                if c_bit & i_bit == 0:
                    next_c = c - val
                    if len(sums_reverse) == k and -next_c < sums_reverse[0]:
                        break
                    next_c_bit = c_bit | i_bit
                    next_sums = (next_c, next_c_bit)
                    if next_sums not in done:
                        done.add(next_sums)
                        heappush(sums, next_sums)
                        heappush(sums_reverse, -next_c)
                        if len(sums_reverse) > k:
                            heappop(sums_reverse)
        return sums_reverse[0]
