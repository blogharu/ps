class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        temp = []

        for c in s:
            if c != ' ':
                temp.append(c)
            else:
                answer.append("".join(reversed(temp)))
                temp = []
        if temp:
            answer.append("".join(reversed(temp)))
        return " ".join(answer)
        