from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max, cur_min = 0, 10**5
        maxs, mins = deque(), []
        for i in range(len(prices)):
            cur_max = max(cur_max, prices[len(prices)-i-1])
            cur_min = min(cur_min, prices[i])
            mins.append(cur_min)
            maxs.appendleft(cur_max)
        answer = 0
        for i in range(len(mins)-1):
            answer = max(answer, maxs[i+1] - mins[i])
        return answer