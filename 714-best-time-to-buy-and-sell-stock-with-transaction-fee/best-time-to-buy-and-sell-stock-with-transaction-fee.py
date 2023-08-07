from functools import cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def get_answer(i, has_stock):
            answer = 0
            if i != len(prices):
                answer = get_answer(i+1, has_stock)
                if has_stock:
                    answer = max(answer, prices[i] - fee + get_answer(i+1, not has_stock))
                else:
                    answer = max(answer, -prices[i] + get_answer(i+1, not has_stock))
            return answer
        for i in range(len(prices)-1, -1, -1):
            get_answer(i, True)
            get_answer(i, False)
        return get_answer(0, False)
        