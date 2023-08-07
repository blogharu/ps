from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = defaultdict(int)
        def get_answer(i, j):
            if (i, j) not in cache and not (i == len(text1) or j == len(text2)):
                c1, c2 = text1[i], text2[j]
                answer = get_answer(i+1, j+1)
                if c1 == c2:                
                    answer += 1
                else:
                    try:
                        next_j = text2.index(c1, j+1)
                    except:
                        ...
                    else:
                        answer = max(answer, 1 + get_answer(i+1, next_j+1))
                    try:
                        next_i = text1.index(c2, i+1)
                    except:
                        ...
                    else:
                        answer = max(answer, 1 + get_answer(next_i+1, j+1))
                cache[(i,j)] = answer
            return cache[(i,j)]
        for i in range(len(text1)-1,-1):
            for j in range(len(text2)-1,-1,-1):
                get_answer(i, j)
        return get_answer(0, 0)