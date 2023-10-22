class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        start = k
        end = k
        answer = 0
        val = nums[k]+1
        while not (start == -1 and end == len(nums)):
            vals = []
            if start >= 0 and nums[start] < val:
                vals.append(nums[start])
            if end < len(nums) and nums[end] < val:
                vals.append(nums[end])
            val = max(vals)
            while start >= 0 and nums[start] >= val:
                start -= 1
            while end < len(nums) and nums[end] >= val:
                end += 1
            answer = max(answer, val * (end - start - 1))
        return answer


        