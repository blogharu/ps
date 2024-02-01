class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 == 0:
            nums.sort()
            answer = [
                [nums[i], nums[i+1], nums[i+2]] for i in range(0, len(nums), 3)
            ]
            for ans in answer:
                if ans[2] - ans[0] > k:
                    return []
            return answer 
        return []
            