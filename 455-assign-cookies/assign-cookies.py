class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        g.sort()
        s.sort()
        while g and s:
            if g[-1] <= s[-1]:
                s.pop()
                answer += 1
            g.pop()
        return answer
