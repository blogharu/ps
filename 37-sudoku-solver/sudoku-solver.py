class Solution:    
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_possible(i, j, val):
            for x in range(9):
                if board[i][x] == val or board[x][j] == val:
                    return False
            i -= i%3
            j -= j%3
            for di in range(3):
                for dj in range(3):
                    if board[i+di][j+dj] == val:
                        return False
            return True
        def solve(i, j):
            if j == 9:
                return True
            nextI = (i + 1)%9
            nextJ = j+1 if i == 8 else j
            if board[i][j] == '.':
                for val in "123456789":
                    if is_possible(i, j, val):
                        board[i][j] = val
                        if solve(nextI, nextJ):
                            return True
                        board[i][j] = '.'
                return False
            return solve(nextI, nextJ)
        solve(0, 0)


