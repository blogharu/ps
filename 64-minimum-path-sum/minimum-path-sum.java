class Solution {
    public int minPathSum(int[][] grid) {
        int i, j;
        int m = grid.length;
        int n = grid[0].length;

        for (i=1; i<n; i++)
            grid[0][i] += grid[0][i-1];

        for (i=1; i<m; i++)
            grid[i][0] += grid[i-1][0];

        for (i=1; i<m; i++) {
            for (j=1; j<n; j++) {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }

        return grid[grid.length-1][n-1];
    }
}