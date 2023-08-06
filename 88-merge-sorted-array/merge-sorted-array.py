class Solution:
    def merge(self, answer: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = answer[:-len(nums2)]
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                answer[k] = nums1[i]
                i += 1
            else:
                answer[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            answer[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            answer[k] = nums2[j]
            j += 1
            k += 1

