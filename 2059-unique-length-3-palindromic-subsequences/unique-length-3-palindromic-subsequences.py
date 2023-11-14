class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answers = set()
        pos = {}
        for i, c in enumerate(s):
            if c not in pos:
                pos[c] = [i, i]
            else:
                pos[c][1] = i 
        for c, (start, end) in pos.items():
            if end - start > 1:
                answers |= set(f"{c}{x}{c}" for x in set(s[start+1:end]))
        return len(answers)
        