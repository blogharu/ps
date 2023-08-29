



class Solution {
    // public int ans=Integer.MAX_VALUE;
    public int minPathSum(int[][] grid) {
        int m=grid.length,n=grid[0].length;
        int[][]dp=new int[m][n];
        int ans=solve(grid,m,n,dp,0,0);
        return ans;
    }
    public int solve(int[][]grid,int m,int n,int[][]dp,int i,int j)
    {
        if(i==m-1&&j==n-1)
        {
            return grid[i][j];
        }
        if(dp[i][j]!=0)return dp[i][j];
        int down=Integer.MAX_VALUE,right=Integer.MAX_VALUE;
    if(i<m-1)down=grid[i][j]+solve(grid,m,n,dp,i+1,j);     
        if(j<n-1)right=grid[i][j]+solve(grid,m,n,dp,i,j+1);
        return dp[i][j]=Math.min(right,down);
    }
}