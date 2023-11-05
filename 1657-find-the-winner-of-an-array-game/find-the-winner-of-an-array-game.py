class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        val = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            num = arr[i]
            if num < val:
                wins += 1
            else:
                val = num
                wins = 1
            if wins == k:
                return val
        return val
        