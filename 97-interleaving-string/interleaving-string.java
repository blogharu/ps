class Solution {
    int cache[][][];
    String s1, s2, s3;
    int getAnswer(int i, int j, int k) {
        if (cache[i][j][k] == 0) {
            cache[i][j][k] = (
                k == s3.length() ||
                (i != s1.length() && s1.charAt(i) == s3.charAt(k) && getAnswer(i+1, j, k+1) == 1) ||
                (j != s2.length() && s2.charAt(j) == s3.charAt(k) && getAnswer(i, j+1, k+1) == 1)
            ) ? 1 : 2;                
        }
        return cache[i][j][k];
    }
    public boolean isInterleave(String s1, String s2, String s3) {
        boolean answer = false;
        if (s1.length() + s2.length() == s3.length()) {
            cache = new int[s1.length()+1][s2.length()+1][s3.length()+1];
            this.s1 = s1;
            this.s2 = s2;
            this.s3 = s3;
            answer = getAnswer(0, 0, 0) == 1 ? true : false;
        }
        return answer;
    }
}