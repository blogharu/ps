from collections import deque

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer, vals, i, temp = 0, 0, 0, deque()
        for target in range(1, 100001):
            vals += len(temp)
            while vals > k:
                num = temp.popleft()
                vals -= target - num
            while i < len(nums) and nums[i] == target:
                temp.append(nums[i])
                i += 1
            answer = max(len(temp), answer)
        return answer
