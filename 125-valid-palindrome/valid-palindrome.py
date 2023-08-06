from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = deque([c for c in s.lower() if c in set("0123456789qwertyuiopasdfghjklzxcvbnm")])
        while len(s) > 1:
            if s.popleft() != s.pop():
                return False
        return True