PUSH = "Push"
POP = "Pop"

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        num = 1
        for t in target:
            while num <= n:
                num += 1
                answer.append(PUSH)
                if num-1 == t:
                    break
                answer.append(POP)
        return answer