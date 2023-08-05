from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()

        counter = Counter(nums)
        nums = sorted(counter.keys())

        for num in counter:
            counter[num] -= 1
            for prev in nums:
                if counter[prev] > 0:
                    counter[prev] -= 1
                    target = -(prev+num)
                    if counter.get(target, 0) > 0:
                        answers.add(tuple(sorted([prev, num, target])))
                        print(prev, num, target)
                    counter[prev] += 1
                if prev == num:
                    break
            counter[num] += 1

        return [list(answer) for answer in answers]
