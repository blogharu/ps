class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def get_answer(i, k, is_stock):
            if i == len(prices):
                return 0
            answer = get_answer(i+1, k, is_stock)
            if is_stock:
                answer = max(answer, get_answer(i+1, k, not is_stock)+prices[i])
            elif k:
                answer = max(answer, get_answer(i+1, k-1, not is_stock)-prices[i])
            return answer
        return get_answer(0, 2, False)