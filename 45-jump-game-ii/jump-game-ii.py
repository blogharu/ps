class Solution:
    def jump(self, nums: List[int]) -> int:
        length, step = len(nums), 0
        if length <= 1:
            return 0
        if nums[0] >= length - 1:
            return 1
        dp = []
        dp.append((0, nums[0]))
        step = 1
        while dp[0][0] < length - 1:
            idx, num = dp.pop()
            max_idx, temp = 0, 0
            for cur_idx, cur_num in enumerate(nums[idx + 1: idx + num + 1]):
                if cur_num + cur_idx > temp:
                    temp = cur_num + cur_idx
                    max_idx = cur_idx
            # print(f"{max_idx + idx + 1}, {nums[max_idx + idx + 1]}")
            dp.append((max_idx + idx + 1, nums[max_idx + idx + 1]))
            step += 1
            if max_idx + idx + 1 + nums[max_idx + idx + 1] >= length - 1:
                break
        return step