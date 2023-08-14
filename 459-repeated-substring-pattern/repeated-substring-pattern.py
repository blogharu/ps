import re

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) > 1:
            if len(set(s)) == 1:
                return True
            for i in range(2, len(s)//2+1):
                if len(s) % i == 0 and len(s) // i == (len(match) if (match := re.findall(s[:i], s)) else -1):
                    return True
        return False

