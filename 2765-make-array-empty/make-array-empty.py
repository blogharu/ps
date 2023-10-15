class Solution:
    def countOperationsToEmptyArray(self, nums_origin: List[int]) -> int:
        answer = len(nums_origin)
        bit_mask = 1 << len(nums_origin) * 2
        base = (1 << len(nums_origin)) + 1
        nums = sorted([(num, i) for i, num in enumerate(nums_origin)])
        prev = 0
        if nums[0][1] == 0:
            nums.pop(0) 
            bit_mask |= base
        for (num, i) in nums:
            ii = i if prev < i else i + len(nums_origin)
            answer += ii - prev - ((bit_mask >> prev) & ((1 << (ii-prev+1)) - 1)).bit_count()
            bit_mask |= base << i
            prev = i
        return answer
