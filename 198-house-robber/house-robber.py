class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[-3] += nums[-1]
        for i in range(len(nums)-4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])