class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer = []
        for x in range(len(img)):
            row = []
            for y in range(len(img[0])):
                total = 0
                count = 0
                for dx in range(-1, 2):
                    nx = x + dx
                    if 0 <= nx < len(img):
                        for dy in range(-1, 2):
                            ny = y + dy
                            if 0 <= ny < len(img[0]):
                                total += img[nx][ny]
                                count += 1
                row.append(total // count)
            answer.append(row)
        return answer
        