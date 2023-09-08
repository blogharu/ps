class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(new ArrayList<Integer>());
        answer.get(0).add(1);
        for (int i=1; i<numRows; i++) {
            List<Integer> prev = answer.get(i-1);
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j=0; j<prev.size()-1; j++) {
                row.add(prev.get(j)+prev.get(j+1));
            }
            row.add(1);
            answer.add(row);
        }

        return answer;
    }
}