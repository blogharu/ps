class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left, right+1):
            is_answer = True
            ds = set(str(num))
            if "0" not in ds:
                for d in set(str(num)):
                    if num % int(d) != 0:
                        is_answer = False
                        break
                if is_answer:
                    answer.append(num)
        return answer