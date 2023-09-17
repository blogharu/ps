class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        answer = 0
        nodes = {(1<<i, i) for i in range(len(graph))}
        next_nodes = set()
        target = (1 << len(graph)) - 1
        done = {}
        while nodes:
            node = nodes.pop()
            if node not in done:
                done[node] = answer
                for next_node in graph[node[1]]:
                    next_mask = node[0] | (1<<next_node)
                    if next_mask == target:
                        return answer+1
                    next_nodes.add((node[0] | 1<<next_node, next_node))
            if not nodes:
                nodes = next_nodes
                next_nodes = set()
                answer += 1 
        return 0
