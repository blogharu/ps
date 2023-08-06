class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == val:
                nums[i] = nums.pop()
            else:
                i += 1
        if nums and nums[-1] == val:
            nums.pop()
        return len(nums)
