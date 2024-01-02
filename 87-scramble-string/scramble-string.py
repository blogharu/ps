from functools import cache
#532

from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        answer = False
        if Counter(s1) == Counter(s2):
            @cache
            def get_answer(s1, s2):
                if len(s1) != 1 or s1 != s2:
                    s1_r = Counter()
                    s2_r = Counter()
                    s2_l = Counter()
                    for i in range(len(s1)-1):
                        s1_r[s1[i]] += 1
                        s2_r[s2[i]] += 1
                        s2_l[s2[-i-1]] += 1
                        if s1_r == s2_r and get_answer(s1[:i+1],s2[:i+1]) and get_answer(s1[i+1:],s2[i+1:]):
                            return True
                        if s1_r == s2_l and get_answer(s1[:i+1],s2[-i-1:]) and get_answer(s1[i+1:],s2[:-i-1]):
                            return True
                    return False
                return True
            answer = get_answer(s1, s2)
        return answer
        