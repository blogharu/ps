class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = defaultdict(list)
        cs = {c:i for i, c in enumerate("qwertyuiopasdfghjklzxcvbnm")}
        temp = [0] * 26
        for s in strs:
            for c in s:
                temp[cs[c]] += 1
            answers[tuple(temp)].append(s)
            for i in range(len(temp)):
                temp[i] = 0
        return [answer for answer in answers.values()]

        