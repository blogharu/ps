class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        answer = float('-inf')
        nums.sort()
        for i in range(len(nums)//2):
            answer = max(nums[i]+nums[-i-1], answer)
        return answer
