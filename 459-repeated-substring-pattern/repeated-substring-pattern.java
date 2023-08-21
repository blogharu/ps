class Solution {
    public boolean repeatedSubstringPattern(String s) {
        boolean answer = false;
        for (int i = 1; i <= s.length() / 2; i++) {
            if (s.length() % i == 0) {
                answer = String.join("", s.split(s.substring(0, i))).length() == 0;
                if (answer) break;
            }
        }
        return answer;        
    }
}