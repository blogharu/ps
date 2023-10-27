from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp = deque()
        for a in range(n//2):
            b = n-a-1
            for x in range(a, b):
                temp.append(matrix[a][x])
            for x in range(a, b+1):
                temp.append(matrix[x][b])
                matrix[x][b] = temp.popleft()
            for x in range(b-1, a-1, -1):
                temp.append(matrix[b][x])
                matrix[b][x] = temp.popleft()
            for x in range(b-1, a, -1):
                temp.append(matrix[x][a])
                matrix[x][a] = temp.popleft()
            for x in range(a, b):
                matrix[a][x] = temp.popleft()        