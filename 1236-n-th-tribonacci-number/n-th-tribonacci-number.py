class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        if n == 3: return 2
        arr = [0, 1, 1]
        for i in range(3, n):
            tot = sum(arr[-3:])
            arr.append(tot)

        return sum(arr[-3:])