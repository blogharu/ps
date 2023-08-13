class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-2] = len(set(nums[-2:])) == 1
        if len(nums) > 2:
            dp[-3] = len(set(nums[-3:])) == 1 or (nums[-3] == nums[-2] -1 and nums[-2] == nums[-1]-1)
        for i in range(len(nums)-4, -1, -1):            
            dp[i] = (dp[i+2] and len(set(nums[i:i+2])) == 1) or (dp[i+3] and (
                (nums[i] == nums[i+1] -1 and nums[i+1] == nums[i+2]-1) or (len(set(nums[i:i+3])) == 1)
            ))
        return dp[0]

