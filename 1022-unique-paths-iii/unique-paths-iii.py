class Solution:
    def uniquePathsIII(self, grid_list: List[List[int]]) -> int:
        grid = {}
        num_nodes = 2
        for i, row in enumerate(grid_list):
            for j, val in enumerate(row):
                grid[(i,j)] = val
                if val == 1:
                    start = (i,j)
                elif val == 2:
                    target = (i,j)
                elif val == 0:
                    num_nodes += 1
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        done = {start}
        self.answer = 0
        def dfs(node):
            if node == target:
                self.answer += len(done) == num_nodes
            else:
                for d in range(4):
                    next_node = (node[0]+dx[d], node[1]+dy[d])
                    if next_node in grid and next_node not in done and  grid[next_node] != -1:
                        done.add(next_node)
                        dfs(next_node)
                        done.remove(next_node)
        dfs(start)
        return self.answer