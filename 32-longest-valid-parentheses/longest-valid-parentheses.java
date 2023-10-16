class Solution {
    public int longestValidParentheses(String s) {
        int[] answers = new int[s.length()];
        int[] stack = new int[s.length()+1];
        Arrays.fill(stack, -1);
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                count++;
                stack[count] = i;
            }
            else if (count > 0) {
                answers[stack[count]] = i - stack[count] + 1;
                count--;
            }
        }
        int i = 0, answer = 0;
        while (i < s.length()) {
            int curAnswer = 0;
            while (i < s.length() && answers[i] != 0) {
                curAnswer += answers[i];
                i += answers[i];
            }
            answer = Math.max(answer, curAnswer);
            i++;
        }
        return answer;
    }
}