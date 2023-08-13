class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        start, end = 0, len(nums)-1
        answer = len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] >= target:
                end = mid - 1
                answer = mid
            else:
                start = mid + 1
        return answer