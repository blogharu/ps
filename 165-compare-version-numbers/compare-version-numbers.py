from collections import deque

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = deque(map(int, version1.split(".")))
        v2 = deque(map(int, version2.split(".")))

        while v1 and v2:
            n1, n2 = v1.popleft(), v2.popleft()
            if n1 == n2:
                continue
            return 1 if n1 > n2 else -1        

        if sum(v1):
            return 1
        elif sum(v2):
            return -1
        return 0