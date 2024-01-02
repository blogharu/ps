from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        answer = [[] for _ in range(max(counts.values()))]
        for num, count in counts.items():
            for i in range(count):
                answer[i].append(num)
        return answer
        

        