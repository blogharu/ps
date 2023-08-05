from decimal import Decimal

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        num_minus = 0
        if numerator < 0:
            numerator *= -1
            num_minus += 1
        if denominator < 0:
            denominator *= -1
            num_minus += 1

        result, remainder = str(numerator // denominator), numerator % denominator
        cache = {}
        floats = []
        num_repeat = 0

        while remainder > 0:
            length = 0
            temp = remainder
            while temp < denominator:
                temp *= 10
                length += 1
            cache[remainder] = str(temp // denominator).zfill(length)
            floats.append(cache[remainder])
            remainder = temp % denominator

            if remainder in cache:
                temp = remainder
                num_repeat = 0
                while 1:
                    num_repeat += 1
                    while temp < denominator:
                        temp *= 10
                    temp %= denominator 
                    if temp == remainder:
                        break
                break
        if remainder == 0:
            result = result if not floats else f'{result}.{"".join(floats)}'
        else:
            result = f'{result}.{"".join(floats[:-num_repeat])}({"".join(floats[-num_repeat:])})'

        return result if num_minus % 2 == 0 else f"-{result}"
