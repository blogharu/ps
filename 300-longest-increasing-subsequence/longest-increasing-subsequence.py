from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def get_answer(i):
            return 1 + max(0, 0, *list(get_answer(j) for j in range(i+1, len(nums)) if nums[i] < nums[j]))
        return max(get_answer(i) for i in range(len(nums)-1, -1, -1))
        