class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        answer = 0
        while children > 0 and money >= 7:
            children -= 1
            money -= 7
            answer += 1
        return answer - ((children == 0 and money > 0) or (children == 1 and money == 3))
        