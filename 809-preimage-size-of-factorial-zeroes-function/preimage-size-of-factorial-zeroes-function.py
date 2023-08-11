from functools import cache

class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        @cache
        def get_answer(val):
            if val == 0:
                return 0
            return val + get_answer(val // 5)

        start, end = 1, k
        while start <= end:
            mid = (start+end) // 2
            answer = get_answer(mid)
            if answer < k:
                start = mid + 1
            elif answer > k:
                end = mid - 1
            else:
                return 5

        return 0 if k else 5