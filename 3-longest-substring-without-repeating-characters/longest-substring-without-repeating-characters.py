from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        answer = -1
        history = deque()
        cs = set()

        for c in s:
            if c in cs:
                answer = max(answer, len(cs))
                while 1:
                    ele = history.popleft()
                    cs.remove(ele)
                    if ele == c:
                        break
            cs.add(c)
            history.append(c)

        return max(answer, len(cs))
