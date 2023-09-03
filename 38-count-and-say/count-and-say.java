class Solution {
    public String countAndSay(int n) {
        String answer = "1";
        for (; n > 1; n--) {
            StringBuilder sb = new StringBuilder();
            char prev = answer.charAt(answer.length()-1);
            int count = 1;
            for (int i=answer.length()-2; i>=0; i--) {
                char cur = answer.charAt(i);
                if (cur == prev) count++;
                else {
                    sb.insert(0, prev);
                    sb.insert(0, count);
                    prev = cur;
                    count = 1;
                }
            }
            sb.insert(0, prev);
            sb.insert(0, count);
            answer = sb.toString();
        }
        return answer;
    }
}