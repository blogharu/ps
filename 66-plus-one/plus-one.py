class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(c) for c in "".join([str(c) for c in str(1+int("".join([str(digit) for digit in digits])))])]