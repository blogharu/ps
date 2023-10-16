class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    public List<List<Integer>> permute(int[] nums) {
        function(nums, 0);
        return ans;
    }

    public void function(int[] arr, int start) {
        if (start == arr.length) {
            List<Integer> list = new ArrayList();
            for (int i = 0; i < arr.length; i++) list.add(arr[i]);
            ans.add(list);
            return;
        }

        for (int i = start; i < arr.length; i++) {
            swap(arr, start, i);
            function(arr, start + 1);
            swap(arr, start, i);
        }
    }

    public void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}