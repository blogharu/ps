class Solution {
    int[] nums;
    List<List<Integer>> answer = new ArrayList<>();
    Set<Integer> unused = new HashSet<>();
    Stack<Integer> temp = new Stack<>();
    public void getAnswer(int n) {
        if (n != 0) {
            for (int i = 0; i < nums.length; i++) {
                if (unused.contains(i)) {
                    unused.remove(i);
                    temp.push(nums[i]);
                    getAnswer(n-1);
                    temp.pop();
                    unused.add(i);
                }
            }
        }
        else
            answer.add(new ArrayList(temp));
    }
    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        for (int i = 0; i < nums.length; i++) unused.add(i);
        getAnswer(nums.length);
        return answer;
    }
}