from functools import cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = {}
        for i, c in enumerate(ring):
            if c not in pos:
                pos[c] = []
            pos[c].append(i)

        @cache
        def get_distance(i, j):
            if i > j:
                i, j = j, i
            return min(abs(i-j), abs(i-j+len(ring)))
        
        nodes = {0: 0}
        next_nodes = {}

        for c in key:
            for i in pos[c]:
                min_count = float('inf')
                for j, count in nodes.items():
                    min_count = min(min_count, count+get_distance(i, j) + 1)
                next_nodes[i] = min_count
            nodes = next_nodes
            next_nodes = {}
        return min(nodes.values())
