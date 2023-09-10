class Solution {
    int MOD = 1000000007;
    public int countOrders(int n) {
        long answer = 1;
        for (int i=1; i<n*2; i+=2)
            answer = (answer * i * (i+1)/2) % MOD;
        return (int) answer;
    }
}