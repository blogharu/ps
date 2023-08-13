class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        answer = -float('inf')
        for sign1, sign2 in [(1,1),(-1,1),(1,-1),(-1,-1)]:
            min_val, max_val = float('inf'), -float('inf')
            for i, (val1, val2) in enumerate(zip(arr1, arr2)):
                val = i + val1 * sign1 + val2 * sign2
                min_val = min(min_val, val)
                max_val = max(max_val, val)
            answer = max(answer, max_val-min_val)
        return answer
                