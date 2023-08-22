from functools import cache

class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        @cache
        def get_answer(i, j):        
            if i == len(text1):
                return len(text2) - j
            elif j == len(text2):
                return len(text1) - i
            elif text1[i] == text2[j]:
                return get_answer(i+1, j+1)
            return min(
                get_answer(i, j+1),
                get_answer(i+1, j+1),
                get_answer(i+1, j),
            ) + 1
        return get_answer(0, 0)
        