from functools import cache
import sys
sys.setrecursionlimit = 1**10

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def get_answer(is_product: bool, k: int, i: int):
            if (k == 0 and not is_product) or len(prices) == i:
                return 0
            result = get_answer(is_product, k, i+1)
            if is_product:
                result = max(result, get_answer(False, k, i+1) + prices[i])
            elif k > 0:
                result = max(result, get_answer(True, k-1, i+1) - prices[i])
            return result
        return get_answer(0, k, 0)
