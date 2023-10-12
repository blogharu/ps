class Solution:
    def checkPartitioning(self, s: str) -> bool:

        firsts_end, thirds_start = [], []
        
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                firsts_end.append(i)
        
        for i in range(len(s)):
            if s[i:] == s[i:][::-1]:
                thirds_start.append(i)
        
        # check
        for f in firsts_end:
            for t in reversed(thirds_start):
                second = s[f+1:t]
                if second == '': break
                if second == second[::-1]:
                    return True

        # return 
        return False 