from functools import cache
from itertools import combinations

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        @cache
        def to_num(row):
            return int("".join(str(v) for v in row), 2)
        counts = {}
        for i, row in enumerate(grid):
            key = to_num(tuple(row))
            if key not in counts:
                counts[key] = i
        if 0 in counts:
            return [counts[0]]
        n = len(grid[0])
        x = (1 << n) - 1
        for i in range(1, 2 if n < 4 else 3):
            for comb in combinations(range(n), i):
                num = to_num(tuple(1 if i in comb else 0 for i in range(n)))
                xor = num ^ x
                A = -1
                B = -1
                for key, val in counts.items():
                    if ((key & num) > 0) and ((key & xor) == 0):
                        A = val
                    elif ((key & xor) > 0) and ((key & num) == 0):
                        B = val
                if A != -1 and B != -1:
                    return sorted([A, B])
        return []
