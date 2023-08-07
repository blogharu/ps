from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        if len(counter) == 1:
            return True
        counter = Counter(counter.values())
        if len(counter) == 1:
            return 1 in counter
        if len(counter) == 2:
            if counter.get(1) == 1:
                return True
            keys = sorted(counter.keys())
            return keys[0] == keys[1]-1 and counter[keys[1]] == 1
        return False