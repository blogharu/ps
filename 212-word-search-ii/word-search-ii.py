from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answers = []

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
                if (nx, ny) not in stack and 0<=nx<len(board) and 0<=ny<len(board[0]):
                    c = board[nx][ny]
                    if c in trie:
                        answer.append(c)
                        stack.add((nx, ny))
                        dfs(trie[c], nx, ny)
                        stack.remove((nx, ny))
                        answer.pop()
                        if len(trie[c]) == 0:
                            del trie[c]
            return False
        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c in trie:
                    answer.append(c)
                    stack.add((i, j))
                    dfs(trie[c], i, j)
                    stack.remove((i, j))
                    answer.pop()
        return answers