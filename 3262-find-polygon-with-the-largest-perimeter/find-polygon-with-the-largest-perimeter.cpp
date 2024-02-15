class Solution {
public:
    long long largestPerimeter(vector<int>& int_nums) {
        std::vector<long long> nums(std::begin(int_nums), std::end(int_nums));
        int idx = nums.size()-1;
        long long sum = std::reduce(nums.begin(), nums.end());
        std::sort(nums.begin(), nums.end());
        while (idx >= 2) {
            if (sum > (nums[idx] << 1)) return sum;
            sum -= nums[idx--];
        }
        return -1;
    }
};