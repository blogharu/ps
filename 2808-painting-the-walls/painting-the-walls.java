class Solution {
    int MAX_VALUE = 600000000;
    int[][] dp;
    int[] cost;
    int[] time;
    public int getAnswer(int i, int t) {
        if (t >= dp.length) { return 0; }
        else if (i == dp.length) { return MAX_VALUE; }
        if (dp[i][t] == 0) {
            dp[i][t] = Math.min(
                getAnswer(i+1, t),
                getAnswer(i+1, t+1+time[i]) + cost[i]
            );
        }
        return dp[i][t];
    }
    public int paintWalls(int[] cost, int[] time) {
        this.cost = cost;
        this.time = time;
        dp = new int[cost.length][cost.length];
        for (int i=cost.length-1; i >= 0; i--) {
            for (int j=cost.length-1; j >= 0; j--) {
                getAnswer(i, j);
            }
        }
        return getAnswer(0, 0);
    }
}