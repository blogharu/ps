from collections import deque

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        answer = 10**10
        selected = deque()
        total = 0
        
        for num in nums:
            total += num
            selected.append(num)
            while total-selected[0] >= target:
                total -= selected.popleft()
            if total >= target:
                answer = min(len(selected), answer)

        return answer if answer != 10**10 else 0