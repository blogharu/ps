class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        min_num = -200
        min_index = 0
        for num in nums:
            if num > min_num:
                min_num = num
                nums[min_index] = num
                min_index += 1
        return min_index