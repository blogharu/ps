from collections import deque

class Solution:
    def myAtoi(self, s: str) -> int:
        s = deque(s)
        answer = []
        while s:
            if s[0] != ' ':
                break
            s.popleft()
        if s and s[0] in {"-", "+"}:
            answer.append(s.popleft())
        while s:
            if s[0] not in set("0123456789"):
                break
            answer.append(s.popleft())
        try:
            answer = int("".join(answer))
        except:
            answer = 0
        else:
            answer = max(-2**31, min(2**31-1, answer))
        return answer