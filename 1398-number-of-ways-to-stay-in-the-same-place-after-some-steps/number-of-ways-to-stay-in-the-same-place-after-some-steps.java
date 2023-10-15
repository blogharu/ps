class Solution {
    int MOD = 1000000007;
    public int numWays(int steps, int arrLen) {
        int[][] counts = new int[2][arrLen];
        int cur = 0;
        counts[cur][0] = 1;
        for (int i = 0; i < steps; i++) {
            int next = (cur+1)%2;
            for (int j = 0; j < Math.min(arrLen, steps-i); j++) {
                counts[next][j] = counts[cur][j];
                if (j > 0) 
                    counts[next][j] = (counts[next][j]+counts[cur][j-1]) % MOD;
                if (j < arrLen-1) 
                    counts[next][j] = (counts[next][j]+counts[cur][j+1]) % MOD;                
            }
            cur = next;
        }
        return counts[cur][0];
    }
}