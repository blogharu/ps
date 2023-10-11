class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        answer = []
        ds = [(1,0),(0,1)]
        def is_left_top(i, j):
            for di, dj in ds:
                if i-di < 0 or j-dj < 0:
                    continue
                else:
                    if land[i-di][j-dj] == 1:
                        return False
            return True
        def get_sums(i, j):
            sums = 0
            for di, dj in ds:
                try:
                    sums += land[i+di][j+dj]
                except:
                    continue
            return sums
        def count_right(i, j):
            count = 0
            for nj in range(j+1, len(row)):
                if row[nj]:
                    count += 1
                else:
                    break
            return count
        def count_down(i, j):
            count = 0
            for ni in range(i+1, len(land)):
                if land[ni][j]:
                    count += 1
                else:
                    break
            return count 
        for i, row in enumerate(land):
            for j, val in enumerate(row):
                if val == 1 and is_left_top(i, j):
                    answer.append([i,j,i+count_down(i, j),j+count_right(i,j)])
        return answer
        