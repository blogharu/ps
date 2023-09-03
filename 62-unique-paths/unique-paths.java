class Solution {
    int MOD = 2 * (int) Math.pow(10, 9);
    public int uniquePaths(int m, int n) {
        int answer = 1;
        if (m != 1 && n != 1) {
            int [][]board = new int[m][n];
            Arrays.fill(board[0], 1);
            for (int i = 0; i < m; i++) board[i][0] = 1;
            for (int i = 1; i < m; i++)
                for (int j = 1; j < n; j++)
                    board[i][j] = (board[i-1][j] + board[i][j-1]) % MOD;
            answer = board[m-1][n-1];
        }
        return answer;
    }
}