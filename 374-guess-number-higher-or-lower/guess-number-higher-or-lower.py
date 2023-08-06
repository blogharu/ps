class Solution:
    def guessNumber(self, end: int) -> int:
        start = 1
        while start <= end:
            mid = (start+end) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                end = mid - 1
            else:
                start = mid + 1
