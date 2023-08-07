class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        while len(cost) > 2:
            cost[-3] += min(cost[-1], cost[-2])
            cost.pop()
        return min(cost)

