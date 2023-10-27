class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 1 and int(num1) == 0 or len(num2) == 1 and int(num2) == 0:
            return "0"
        num1 = [int(c) for c in num1]
        num2 = [int(c) for c in num2]
        nums = [0] * (len(num1)+len(num2)+1)
        for i in range(len(num1)):
            n1 = num1[-i-1]
            for j in range(len(num2)):
                n2 = num2[-j-1]
                x = i + j
                nums[x] += n1 * n2
                while nums[x] >= 10:
                    nums[x+1] += nums[x] // 10
                    nums[x] %= 10
                    x += 1
        while nums[-1] == 0:
            nums.pop()

        return "".join(str(num) for num in nums[::-1])
        