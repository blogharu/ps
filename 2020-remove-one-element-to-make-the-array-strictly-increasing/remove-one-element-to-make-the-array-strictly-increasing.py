from functools import cache

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        @cache
        def is_answer(start, end):
            return True if (start == end) else (
                (is_answer(start, end-1) and nums[end-1] < nums[end]) if (start == 0) else (
                    is_answer(start+1, end) and nums[start] < nums[start+1]
                )
            )
        if len(nums) == 1 or is_answer(0, len(nums)-2) or is_answer(1, len(nums)-1):
            return True
        else:
            for i in range(1, len(nums)-1):
                if is_answer(0, i-1) and is_answer(i+1, len(nums)-1) and nums[i-1] < nums[i+1]:
                    return True
        return False