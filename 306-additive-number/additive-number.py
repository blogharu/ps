from functools import cache

class Solution:
    def isAdditiveNumber(self, str_num: str) -> bool:
        @cache
        def get_num(start, end):
            num = int(str_num[start:end])
            return num if len(str(num)) == end-start else -1

        @cache
        def is_additive_number(s0, s1, s2, end):
            num0 = get_num(s0, s1)
            num1 = get_num(s1, s2)
            num2 = get_num(s2, end)
            if num0 >= 0 and num1 >= 0 and num2 >= 0 and num0 + num1 == num2:
                return True
            return False
        
        @cache
        def is_additive_sequence(s0, s1, s2, end):
            if is_additive_number(s0, s1, s2, end):
                if end == len(str_num):
                    return True
                for next_end in range(end+1, len(str_num)+1):
                    if is_additive_sequence(s1, s2, end, next_end):
                        return True
            return False
        
        s0 = 0
        for s1 in range(s0+1, len(str_num)+1):
            for s2 in range(s1+1, len(str_num)+1):
                for end in range(s2+1, len(str_num)+1):
                    if is_additive_sequence(s0, s1, s2, end):
                        return True
        return False