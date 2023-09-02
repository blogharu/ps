class Solution {
    public int minExtraChar(String s, String[] dictionary) {
        Set<String> dict = new HashSet<>(Arrays.asList(dictionary));
        int []dp = new int[s.length()];
        Arrays.fill(dp, -1);
        return getAnswer(dp, dict, s, 0);
    }
    public int getAnswer(int []dp, Set<String> dictionary, String s, int i) {
        if (i >= dp.length) return 0;
        if (dp[i] == -1) {
            dp[i] = 1 + getAnswer(dp, dictionary, s, i+1);
            for (int j=i+1; j<s.length()+1; j++) {
                String subString = s.substring(i, j);
                if (dictionary.contains(subString)) {
                    dp[i] = Math.min(dp[i], getAnswer(dp, dictionary, s, j));
                }
            }
        }
        return dp[i];
    }
}