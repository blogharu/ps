class Solution:
    def minOperations(self, s: str) -> int:
        counts = [0, 0]
        for i, c in enumerate(s):
            for j in range(2):
                counts[j] += str((i+j)%2) == c
        return min(counts)

        