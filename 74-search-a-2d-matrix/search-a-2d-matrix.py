class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get(i):
            return matrix[i // len(matrix[0])][i % len(matrix[0])]
        start, end = 0, len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = (start+end) // 2
            val = get(mid)
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False