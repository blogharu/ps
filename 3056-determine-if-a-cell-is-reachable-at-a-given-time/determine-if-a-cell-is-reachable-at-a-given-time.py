class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return max(abs(sx-fx), abs(sy-fy)) <= t and not (t == 1 and sx == fx and sy == fy)
        