# 8:36

one_map = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
two_special_map = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}
two_map = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        def convert_three(num):
            answer = []
            if num >= 100:
                answer.append(one_map[num//100])
                answer.append("Hundred")
                num %= 100
            if num in two_special_map:
                answer.append(two_special_map[num])
            else:
                if num > 10:
                    answer.append(two_map[num//10])
                    num %= 10
                if num in one_map:
                    answer.append(one_map[num])
            return " ".join(answer)
        suffixes = ["Billion", "Million", "Thousand", ""]
        answer = []
        while num:
            suffix = suffixes.pop()
            converted = convert_three(num % 1000)
            if converted:
                if suffix:
                    answer.append(suffix)
                answer.append(converted)
            num //= 1000
        return " ".join(reversed(answer))
        