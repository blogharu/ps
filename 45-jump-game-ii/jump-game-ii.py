class Solution:
    def jump(self, nums: List[int]) -> int:
        answers = {0:0}
        for i in range(len(nums)):
            answer = answers[i]
            for j in range(i+1, i+1+nums[i]):
                if j in answers:
                    answers[j] = min(answers[j],answer + 1)             
                else:
                    answers[j] = answer + 1
        return answers[len(nums)-1]
