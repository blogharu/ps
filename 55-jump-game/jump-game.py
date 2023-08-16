class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0 
        max_jump = 0
        while i < len(nums) and i <= max_jump:
            max_jump = max(i+nums[i], max_jump)
            i += 1
        return max_jump >= len(nums) - 1
