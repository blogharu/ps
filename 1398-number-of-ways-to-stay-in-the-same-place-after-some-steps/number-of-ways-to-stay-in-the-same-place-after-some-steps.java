class Solution {
    public int numWays(int steps, int arrLen) {
        int[][] counts = new int[2][arrLen];
        counts[0][0] = 1;
        for (int i = 0; i < steps; i++) {
            for (int j = 0; j < Math.min(arrLen, steps-i); j++) {
                counts[(i+1)%2][j] = counts[i%2][j];
                if (j > 0) 
                    counts[(i+1)%2][j] = (counts[(i+1)%2][j]+counts[i%2][j-1]) % 1000000007;
                if (j < arrLen-1) 
                    counts[(i+1)%2][j] = (counts[(i+1)%2][j]+counts[i%2][j+1]) % 1000000007;                
            }
        }
        return counts[steps%2][0];
    }
}