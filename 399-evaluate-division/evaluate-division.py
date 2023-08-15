from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dones = defaultdict(dict)
        edges = defaultdict(dict)
        for (x, y), value in zip(equations, values):
            edges[x][y] = value
            edges[y][x] = 1 / value

        answer = []
        for start, target in queries:
            if start not in dones and start in edges:
                done = dones[start]
                nodes = [(start, 1)]
                while nodes:
                    node, val = nodes.pop()
                    if node not in done:
                        done[node] = val
                        for next_node, c in edges[node].items():
                            nodes.append((next_node, val*c))                                
            answer.append(dones[start].get(target, -1))
        return answer