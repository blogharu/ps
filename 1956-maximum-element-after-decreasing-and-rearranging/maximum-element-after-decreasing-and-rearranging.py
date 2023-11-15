class Solution:
    def maximumElementAfterDecrementingAndRearranging(
        self, 
        arr: List[int],
    ) -> int:
        nums = {}
        for num in arr:
            temp = []
            while num in nums:
                temp.append(num)
                num = nums[num]
            val = num - 1
            if val >= 0:
                nums[num] = val
            for t in temp:
                nums[t] = val
            
        return len(nums)
