from collections import defaultdict

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        answer = 0
        nodes = defaultdict(dict)
        next_nodes = defaultdict(dict)
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == "1":
                    nodes[i][j] = 1

        while nodes:
            answer += 1
            for i, top in nodes.items():
                if i+1 in nodes:
                    bottom = nodes[i+1] 
                    for j in top:
                        if j+1 in top and j in bottom and j+1 in bottom:
                            next_nodes[i][j] = 1
            nodes = next_nodes
            next_nodes = defaultdict(dict)
        
        return answer**2


        