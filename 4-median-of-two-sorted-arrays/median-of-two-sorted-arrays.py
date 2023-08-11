

class Solution:   
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        target = 1 + total // 2
        cur, prev = 0, 0
        while target > 0:
            if not nums1:
                nums = nums2
            elif not nums2:
                nums = nums1
            else:
                nums = nums1 if nums1[-1] > nums2[-1] else nums2
            cur, prev = nums.pop(), cur
            target -= 1
        return cur if total % 2 == 1 else (cur+prev) / 2
