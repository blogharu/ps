class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []

        ds = [(-1, -1), (0, -1), (1, -1)]

        def get_answer(answer):
            if len(answer) == n:
                answers.append(answer.copy())
                return

            y = len(answer)
            for x in range(n):
                is_answer = True
                for dx, dy in ds:
                    nx, ny = x+dx, y+dy
                    while 0 <= nx < n and 0 <= ny and ny < y:
                        if answer[ny][nx] == "Q":
                            is_answer = False
                            break
                        nx, ny = nx+dx, ny+dy
                    if is_answer == False:
                        break
                if is_answer:
                    answer.append(f"{'.'*x}Q{'.'*(n-x-1)}")
                    print(answer)
                    get_answer(answer)
                    answer.pop()

        get_answer([])
        return answers