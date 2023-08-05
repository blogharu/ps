class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, val in enumerate(nums):
            j = cache.get(target - val, None)
            if j is not None:
                return [i, j]
            cache[val] = i