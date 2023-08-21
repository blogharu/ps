interface isRow {boolean run(int x, int y);}
interface isCol {boolean run(int x, int y);}
interface isSquare {boolean run(int x, int y);}

class Solution {
    public boolean isValidSudoku(char[][] board) {
        isRow isRowI = (x, y)->{ 
            for (int i = 0; i < 9; i++)
                if (i != y && board[x][i] == board[x][y]) 
                    return false;
            return true; 
        };
        isCol isColI = (x, y)->{
            for (int i = 0; i < 9; i++)
                if (i != x && board[i][y] == board[x][y]) 
                    return false;
            return true; 
        };
        isSquare isSquareI = (x, y)-> {
            int i = 3 * (x / 3), j = 3 * (y / 3);
            for (int di = 0; di < 3; di++) {
                for (int dj = 0; dj < 3; dj++) {
                    if (i+di != x && j+dj != y && board[i+di][j+dj] == board[x][y])
                        return false;
                }
            }
            return true;
        };
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (
                    board[i][j] != '.' && (
                        !isRowI.run(i, j) || 
                        !isColI.run(i, j) || 
                        !isSquareI.run(i, j)
                    )
                ) return false;
            }
        }
        return true;
    }
}