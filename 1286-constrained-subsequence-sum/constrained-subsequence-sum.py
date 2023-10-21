class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        for i in range(len(nums)):
            if q: nums[i] += q[0]
            while q and q[-1] < nums[i]: q.pop()
            if nums[i] > 0: q.append(nums[i])
            if q and i>=k and q[0] == nums[i-k]:
                q.popleft()
        return max(nums)