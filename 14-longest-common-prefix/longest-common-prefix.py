class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        for tup in zip(*strs):
            c = tup[-1]
            is_same = True
            for i in range(len(tup)-1):
                if tup[i] != c:
                    is_same = False
                    break
            if is_same == False:
                break
            answer.append(c)
            
        return "".join(answer)