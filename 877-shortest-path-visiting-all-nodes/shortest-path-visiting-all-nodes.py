from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodes = deque((1<<i, i, 0) for i in range(len(graph)))
        target = (1 << len(graph)) - 1
        done = set()
        while nodes:
            mask, node, answer = nodes.popleft()
            if (mask, node) not in done:
                done.add((mask, node))
                if mask == target:
                    return answer
                answer += 1
                for next_node in graph[node]:
                    nodes.append((mask | 1<<next_node, next_node, answer))