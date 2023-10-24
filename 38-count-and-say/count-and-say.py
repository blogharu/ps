# 9:36

class Solution:
    def countAndSay(self, n: int) -> str:
        nums = [1]
        for _ in range(n-1):
            next_nums = []
            prev_num = nums[0]
            count = 1
            for i in range(1, len(nums)):
                num = nums[i]
                if num == prev_num:
                    count += 1
                else:
                    next_nums.append(count)
                    next_nums.append(prev_num)
                    prev_num = num
                    count = 1
            next_nums.append(count)
            next_nums.append(prev_num)
            nums = next_nums            
        return "".join([str(num) for num in nums])