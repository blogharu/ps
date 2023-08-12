class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        obstacleGrid[0][0] = -1
        for i, row in enumerate(obstacleGrid):            
            for j, val in enumerate(row):
                if i == 0 and j == 0:
                    continue
                if val == 1:
                    continue
                else:
                    val = 0
                    if i-1 >= 0 and obstacleGrid[i-1][j] != 1:
                        val += obstacleGrid[i-1][j]
                    if j-1 >= 0 and obstacleGrid[i][j-1] != 1:
                        val += obstacleGrid[i][j-1]
                    obstacleGrid[i][j]=val
        return 0 if val >= 0 else -val
