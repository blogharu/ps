class Solution:
    def intToRoman(self, num: int) -> str:
        answer = []

        val_to_sym = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}

        for i, (val, sym) in enumerate(val_to_sym.items()):
            temp = num // val
            if temp:
                answer.append(sym*temp)            
            num %= val      
            if num >= val - (X := val // 10 if i%2 == 0 else val // 5):
                answer.append(val_to_sym[X]+sym)
                num -= val-X
        return "".join(answer)