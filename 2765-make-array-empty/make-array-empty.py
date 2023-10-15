class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        mapping = {}
        for i, num in enumerate(nums):
            mapping[num] = i
        nums.sort()
        # best case requires n steps
        n = len(nums)
        result = n

        for i in range(1, n):
            if mapping[nums[i]] < mapping[nums[i-1]]:
                result += n - i
        return result