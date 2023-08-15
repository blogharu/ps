from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        answer = 0

        connections_dict = defaultdict(set)
        for a, b in connections:
            connections_dict[a].add((a,b))
            connections_dict[b].add((a,b))
        
        nodes = {0}
        while nodes:
            node = nodes.pop()
            if node in connections_dict:
                for start, end in connections_dict.pop(node):
                    next_node = start if node != start else end
                    if next_node in connections_dict:
                        answer += end != node
                        nodes.add(next_node)
        return answer