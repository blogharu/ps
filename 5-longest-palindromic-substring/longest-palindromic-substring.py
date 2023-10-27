class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def is_palindrome(start, end):
            if start < end:
                if s[start] == s[end]:
                    return is_palindrome(start+1,end-1)
                return False
            return True            
        c_to_index = defaultdict(list)
        for i, c in enumerate(s):
            c_to_index[c].append(i)
        answer_start = 0
        answer_end = 0
        for indexes in c_to_index.values():
            for i, start in enumerate(indexes):
                for j in range(i+1, len(indexes)):
                    end = indexes[j]
                    if end - start > answer_end - answer_start and is_palindrome(start, end):
                        answer_start = start
                        answer_end = end
        return s[answer_start:answer_end+1]
        