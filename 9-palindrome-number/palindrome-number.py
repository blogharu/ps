from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        cs = deque(str(x))
        while len(cs) > 1:
            if cs.popleft() != cs.pop():
                return False
        return True