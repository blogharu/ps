class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_bits = len(nums[0])
        answers = set(i for i in range(2**num_bits))
        for num in nums:
            answers.remove(int(num, 2))
        return bin(answers.pop())[2:].zfill(num_bits)
        