class Solution {
    public int combinationSum4(int[] nums, int target) {
        Arrays.sort(nums);
        int []dp = new int[target+1];
        for (int t=1; t<=target; t++) {
            for (int num: nums) {
                if (num < t) {
                    dp[t] += dp[t-num];
                } else {
                    if (num == t) dp[t]++;
                    break;
                }
            }
        }
        return dp[target];
    }
}