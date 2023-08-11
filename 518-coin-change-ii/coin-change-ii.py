class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        cache = {}
        def get_answer(amount, index):
            if (amount, index) not in cache:
                answer = 0
                if amount >= 0 and index != len(coins):
                    if amount == 0:
                        answer = 1
                    elif index < len(coins):
                        answer += get_answer(amount, index+1)
                        answer += get_answer(amount-coins[index], index)                    
                cache[(amount, index)] = answer
            return cache[(amount, index)]
        return get_answer(amount, 0)