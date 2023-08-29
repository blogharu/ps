class Solution {
    public int bestClosingTime(String customers) {
        int sums[] = new int[customers.length()+1];
        for (var i=0; i<customers.length(); i++) {
            sums[i+1] = sums[i] + (customers.charAt(i) == 'Y'?1:0);
        }

        int penalty = customers.length()-sums[customers.length()];
        int answer = customers.length();
        for (int i=customers.length()-1; i>=0; i--) {
            int curPenalty = sums[customers.length()]-sums[i]+i-sums[i];
            if (curPenalty<=penalty) {
                penalty = curPenalty;
                answer = i;
            }
        }

        return answer;
    }
}