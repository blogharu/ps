from functools import cache

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        @cache
        def is_answer(v1, v2, i):
            if i == len(num):
                return True
            elif num[i] == "0":
                if v1 + v2 != 0:
                    return False
            v3 = v1+v2
            if num[i:].startswith(str(v3)):
                return is_answer(v2, v3, i+len(str(v3)))
            return False
        for i in range(1, len(num)):
            if len(num[:i]) == len(str(int(num[:i]))):
                for j in range(i+1, len(num)):
                    if len(num[i:j]) == len(str(int(num[i:j]))):
                        if is_answer(int(num[:i]), int(num[i:j]), j):
                            return True
        return False