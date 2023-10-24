class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in set("({["):
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
        