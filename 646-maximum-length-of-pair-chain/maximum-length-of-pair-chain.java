class Solution {
    public int findLongestChain(int[][] pairs) {
        var dp = new int[2002];
        var minPairs = new int[2001];
        Arrays.fill(minPairs, 3000);

        for (var pair: pairs) 
            minPairs[pair[0]+1000] = Math.min(minPairs[pair[0]+1000], pair[1]+1000);

        for (int i = 1999; i >= 0; i--) {
            if (minPairs[i]!=3000) dp[i] = 1 + dp[minPairs[i]+1];
            dp[i] = Math.max(dp[i], dp[i+1]);
        }

        return dp[0];
    }
}