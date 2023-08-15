from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_orange = 0
        nodes = deque()
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val > 0:
                    if val == 2:
                        nodes.append((x,y,0))
                    num_orange += 1
        answer = 0
        while nodes:
            x, y, count = nodes.popleft()
            if grid[x][y] != 3:
                answer = count
                grid[x][y] = 3
                num_orange -= 1
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        nodes.append((nx,ny,count+1))
        return -1 if num_orange > 0 else answer


