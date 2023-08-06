from heapq import heappush, heappop

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        heap = [0]
        heap_set = {0}
        wordDict = set(wordDict)
        while heap:
            start = heappop(heap)
            for i in range(1, 21):
                next_i = start+i
                if s[start:next_i] in wordDict:
                    if next_i == len(s):
                        return True
                    if next_i not in heap_set:
                        heap_set.add(next_i)
                        heappush(heap, next_i)
        return False