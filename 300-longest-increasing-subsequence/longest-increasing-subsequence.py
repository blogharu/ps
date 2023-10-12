from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def get_answer(i, last):
            temp = 0
            for x in range(i+1, len(nums)):
                if last < nums[x]:
                    temp = max(temp, get_answer(x, nums[x]))
            return 1 + temp
        return max(get_answer(i, nums[i]) for i in range(len(nums)-1, -1, -1))
        