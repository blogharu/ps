class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        min_num = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            num = nums[i]
            if num < min_num:
                min_num = num
            elif num % min_num == 0:
                answer += num // min_num - 1
            else:
                temp = num // min_num
                answer += temp
                min_num = num // (temp + 1)
        return answer
