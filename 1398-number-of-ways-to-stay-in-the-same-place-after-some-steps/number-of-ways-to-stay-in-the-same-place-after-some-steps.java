class Solution {
    long MOD = 1000000007;
    public int numWays(int steps, int arrLen) {
        long[][] counts = new long[2][arrLen+2];
        int cur = 0;
        counts[cur][1] = 1;
        for (int i = 0; i < steps; i++) {
            for (int j = 1; j < Math.min(arrLen+1, steps-i+1); j++) {
                counts[(cur+1)%2][j] = (counts[cur][j]+counts[cur][j-1]+counts[cur][j+1])%MOD;
            }
            cur = (cur+1)%2;
        }
        return (int) counts[cur][1];
    }
}