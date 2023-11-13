from heapq import heappush, heappop

class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        indexes = []
        chars = []
        for i, c in enumerate(s):
            if c in set("aeiouAEIOU"):
                indexes.append(i)
                heappush(chars, c)
        for i in indexes:
            s[i] = heappop(chars)
        return "".join(s)
        