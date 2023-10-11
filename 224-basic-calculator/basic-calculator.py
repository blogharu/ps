class Solution:
    def calculate(self, s: str) -> int:
        def get_answer(start, end):
            print(start, end)
            answer = 0
            ps = 0
            temp = []
            if s[start] == "-":
                temp.append("-")
                start += 1
            i = start
            while i < end:
                c = s[i]
                if not ps and c != "(":
                    if c in {"+", "-"}:
                        if temp:
                            print("X", temp)
                            answer += int("".join(temp))
                        temp = [c]
                    elif c != " ":
                        temp.append(c)
                elif c == "(":
                    if ps == 0:
                        start = i + 1
                    ps += 1
                elif c == ")":
                    ps -= 1
                    if ps == 0:
                        oper = -1 if temp and temp[0] == "-" else 1
                        temp = [str(oper*get_answer(start, i))]
                i += 1
            if temp:
                answer += int("".join(temp))
            print("ANS", answer)
            return answer
        return get_answer(0, len(s))
