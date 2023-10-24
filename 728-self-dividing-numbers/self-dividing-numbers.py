class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left, right+1):
            digits = set(str(num))
            if "0" not in digits:
                is_answer = True
                for str_digit in set(str(num)):
                    if num % int(str_digit) != 0:
                        is_answer = False
                        break
                if is_answer:
                    answer.append(num)
        return answer