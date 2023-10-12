from collections import defaultdict

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def is_palindrome(start, end):
            if start >= len(s):
                return False
            return s[start:end+1] == s[start:end+1][::-1]

        ss = []
        for e in range(len(s)):
            if is_palindrome(0, e):
                ss.append(e+1)

        e = len(s)-1

        es = []
        for st in range(len(s)):
            if is_palindrome(st, e):
                es.append(st-1)
        
        e_start = 0
        for start in ss:
            while e_start < len(es):
                if es[e_start] >= start:
                    break
                e_start += 1
            for x in range(e_start, len(es)):
                end = es[x]
                if is_palindrome(start, end):
                     return True

        return False


        