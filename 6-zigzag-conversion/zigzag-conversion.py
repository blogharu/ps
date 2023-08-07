class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answers = [[] for _ in range(numRows)]
        indexes = [i for i in range(numRows)] + [i for i in range(numRows-2, 0, -1)]
        i = 0
        for c in s:
            answers[indexes[i]].append(c)
            i = (i+1)%len(indexes)
        return "".join(["".join(answer) for answer in answers])
