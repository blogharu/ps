from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def get_answer(i, is_stock: bool):
            if i == len(prices):
                return 0
            answer = get_answer(i+1, is_stock)
            if is_stock:
                answer = max(answer, get_answer(i+1, False) + prices[i])
            else:
                answer = max(answer, get_answer(i+1, True) - prices[i])
            return answer
        return get_answer(0, False)
        