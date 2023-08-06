from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(comb) for comb in combinations([1,2,3,4,5,6,7,8,9], k) if sum(comb) == n]