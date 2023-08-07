class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        answer = sum(nums[-3:])
        score = abs(target-answer)

        def bs(start, target):
            answer = -1
            end = len(nums)-1
            while start <= end:
                mid = (start+end) // 2
                val = nums[mid]
                if val < target:
                    start = mid + 1
                else:
                    answer = mid
                    end = mid - 1
            return answer

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                _answer = nums[i] + nums[j]
                k = bs(j+1, target - _answer - score)
                if k == -1:
                    continue
                for k in range(k, len(nums)):
                    cur_answer = _answer + nums[k]
                    if cur_answer > target + score:
                        break
                    cur_score = abs(target - cur_answer)
                    if cur_score < score:
                        answer= cur_answer
                        score = cur_score

        return answer
