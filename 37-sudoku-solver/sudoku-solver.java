class Solution {
    public boolean isRow(int i, char[][] board, char val) {
        for (int j=0; j < 9; j++)
            if (board[i][j] == val) return false;
        return true;
    }
    public boolean isCol(int j, char[][] board, char val) {
        for (int i=0; i < 9; i++)
            if (board[i][j] == val) return false;
        return true;
    }
    public boolean isSquare(int i, int j, char[][] board, char val) {
        i -= i%3;
        j -= j%3;
        for (int di = 0; di < 3; di++) {
            for (int dj = 0; dj < 3; dj++) {
                if(board[i+di][j+dj] == val) return false;
            }
        }
        return true;
    }
    public boolean isPossible(int i, int j, char[][] board, char val) {
        return isRow(i, board, val) && isCol(j, board, val) && isSquare(i, j, board, val);
    }

    public boolean solve(int i, int j, char[][] board) {
        if (j == 9) return true;
        int nextI = (i+1)%9;
        int nextJ = (i==8) ? j+1 : j;
        if (board[i][j] == '.') {
            for (int val = 1 + '0'; val < 10 + '0'; val++) {
                char cVal = (char) val;
                if (isPossible(i, j, board, cVal)) {
                    board[i][j] = cVal;
                    if (solve(nextI, nextJ, board)) return true;
                    board[i][j] = '.';
                }
            }
            return false;
        }
        return solve(nextI, nextJ, board);
    }
    public void solveSudoku(char[][] board) {
        solve(0, 0, board);
    }
}