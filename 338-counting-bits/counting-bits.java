class Solution {
    public int[] countBits(int n) {
        var answer = new int[n+1];
        var left = 1;
        for (int i=0; i<=n; i++) {
            if (i >> 1 == left) left <<= 1;
            answer[i] = i > 1 ? 1 + answer[i-left] : i;
        }
        return answer;
    }
}