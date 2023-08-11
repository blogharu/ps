from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answers = []

        board = {(i,j):c for i, s in enumerate(board) for j, c in enumerate(s)}
        cs = defaultdict(set)
        for k, v in board.items():
            cs[v].add(k)

        trie = {}
        for word in words:
            temp = trie
            for c in word:
                if c not in temp:
                    temp[c] = {}
                temp = temp[c]
            temp[True] = True

        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = set()
        answer = []
        def dfs(trie, x, y):
            if True in trie:
                answers.append("".join(answer))
                del trie[True]
            for (dx, dy) in ds:
                nx, ny = x+dx, y+dy
                if (nx, ny) not in stack and (nx, ny) in board:
                    c = board[(nx, ny)]
                    if c in trie:
                        answer.append(c)
                        stack.add((nx, ny))
                        dfs(trie[c], nx, ny)
                        stack.remove((nx, ny))
                        answer.pop()
            return False
        
        for c in trie:
            for pos in cs.get(c, []):
                answer.append(c)
                stack.add(pos)
                dfs(trie[c], *pos)
                stack.remove(pos)
                answer.pop()

        return answers