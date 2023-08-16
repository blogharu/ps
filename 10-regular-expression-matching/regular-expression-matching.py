class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        queries = []
        temp = []
        for c in p:
            if temp and c == "*":
                temp2 = temp.pop() + "*"
                if temp:
                    queries.append("".join(temp))
                queries.append(temp2)
                temp = []
            else:
                temp.append(c)
        if temp:
            queries.append("".join(temp))
        def get_answer(si, qi):
            if qi == len(queries):
                return si == len(s) and qi == len(queries)
            query = queries[qi]
            try:
                if query.endswith("*"):
                    is_dot = query[0] == "."
                    while 1:
                        if get_answer(si, qi+1):
                            return True
                        if s[si] != query[0] and not is_dot:
                            break
                        si += 1
                        if si == len(s):
                            return get_answer(si, qi+1)
                else:
                    for a, b in zip(query, s[si:]):
                        if a != "." and a != b:
                            return False
                    return get_answer(si+len(query), qi+1)
            except:
                ...
            return False
            
        return get_answer(0, 0)