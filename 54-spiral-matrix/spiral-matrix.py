# 2:48

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix_dict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix_dict[(i,j)] = matrix[i][j]
        answer = []
        ds = [(0,1),(1,0),(0,-1),(-1,0)]
        d_index = 0
        node = (0,0)
        while matrix_dict:
            answer.append(matrix_dict.pop(node))
            x, y = node
            for i in range(4):
                nx, ny = x+ds[d_index][0], y+ds[d_index][1]
                if (nx, ny) in matrix_dict:
                    break
                d_index = (d_index+1)%4                
            node = (nx, ny)
        return answer
