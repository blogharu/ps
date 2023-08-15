from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ds = [(-1,0),(1,0),(0,-1),(0,1)]
        nodes = deque([(0, *entrance)])
        done = {}

        while nodes:
            steps, x, y = nodes.popleft()
            if (x, y) not in done:
                done[(x, y)] = steps
                for dx, dy in ds:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == ".":
                        if (nx == 0 or nx == len(maze) - 1 or ny == 0 or ny == len(maze[0])-1) and (nx, ny) not in done:
                            return steps + 1
                        nodes.append((steps+1, nx, ny))
        return -1