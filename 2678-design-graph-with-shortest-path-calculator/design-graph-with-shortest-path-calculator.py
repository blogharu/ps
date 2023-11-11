class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.shortest_paths = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        start, end, weight = edge
        if weight < self.shortest_paths[start][end]:
            self.shortest_paths[start][end] = weight
            for a in range(len(self.shortest_paths)):
                to_start = self.shortest_paths[a][start]
                if to_start != float('inf'):
                    for b in range(len(self.shortest_paths)):
                        to_end = self.shortest_paths[end][b]
                        if to_start + to_end + weight < self.shortest_paths[a][b]:
                            self.shortest_paths[a][b] = to_start + to_end + weight

    def shortestPath(self, node1: int, node2: int) -> int:
        return -1 if self.shortest_paths[node1][node2] == float('inf') else self.shortest_paths[node1][node2]



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)