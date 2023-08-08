class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check, i, val = 0, 0, None
        while i < len(nums):
            num = nums[i]
            if num != val:
                val = num
                nums[check] = val
                check += 1
                if i+1 < len(nums) and nums[i+1] == val:
                    nums[check] = val
                    check += 1
            i += 1
        return check