from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if digits:
            chars = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
            }
            temp = deque()
            def _(i):
                if i == len(digits):
                    answer.append("".join(temp))
                else:
                    for c in chars[digits[i]]:
                        temp.append(c)
                        _(i+1)
                        temp.pop()
            _(0)
        return answer
