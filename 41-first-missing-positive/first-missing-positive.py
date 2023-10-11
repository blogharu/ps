# 7:18
# 7:22

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = 1
        while answer in nums:
            answer += 1
        return answer
        