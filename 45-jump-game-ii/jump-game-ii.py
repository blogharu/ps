class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i]:
                nums[i] = 1+min(nums[i+1:i+1+nums[i]])
            else:
                nums[i] = len(nums)
        return nums[0]
