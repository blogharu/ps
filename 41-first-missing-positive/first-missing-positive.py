# 7:18
# 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = {num for num in nums if num > 0}
        answer = 1
        while answer in nums:
            answer += 1
        return answer
        