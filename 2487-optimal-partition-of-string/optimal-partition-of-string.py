class Solution:
    def partitionString(self, s: str) -> int:
        answer = 1
        temp = set()
        for c in s:
            if c not in temp:
                temp.add(c)
            else:
                temp = {c}
                answer += 1
        return answer