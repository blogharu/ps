class Solution {
    int[] nums;
    List<List<Integer>> ans = new ArrayList<>();
    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        function(0);
        return ans;
    }

    public void function(int start) {
        if (start == nums.length) {
            List<Integer> list = new ArrayList();
            for (int i = 0; i < nums.length; i++) list.add(nums[i]);
            ans.add(list);
            return;
        }

        for (int i = start; i < nums.length; i++) {
            swap(start, i);
            function(start + 1);
            swap(start, i);
        }
    }

    public void swap(int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}