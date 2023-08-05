class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        temps = nums[:len(nums)-k]
        del nums[:len(nums)-k]
        nums.extend(temps)