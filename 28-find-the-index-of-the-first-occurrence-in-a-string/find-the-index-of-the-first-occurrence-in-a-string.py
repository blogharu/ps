import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return answer.start() if (answer := re.search(needle, haystack)) else -1