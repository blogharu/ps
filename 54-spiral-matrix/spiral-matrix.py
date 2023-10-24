class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix_dict = {}
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                matrix_dict[(i, j)] = val

        answer = []

        node = (0, 0)
        prev_d = 0
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while node in matrix_dict:
            answer.append(matrix_dict.pop(node))
            for i in range(4):
                d = (prev_d+i)%4
                next_node = (node[0] + ds[d][0], node[1] + ds[d][1])
                if next_node in matrix_dict:
                    node = next_node
                    prev_d = d
        
        return answer