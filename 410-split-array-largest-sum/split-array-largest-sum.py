class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        min_answer = max(nums)
        max_answer = sum(nums)
        answer = max_answer
        def is_possible(target):
            temp = k
            total = 0
            for num in nums:
                if num + total <= target:
                    total = num + total
                else:
                    temp -= 1
                    if temp == 0:
                        return False
                    total = num
            return True
        while min_answer <= max_answer:
            mid_answer = (min_answer+max_answer) // 2
            if is_possible(mid_answer):
                max_answer = mid_answer - 1
                answer = min(answer, mid_answer)
            else:
                min_answer = mid_answer + 1
        return answer