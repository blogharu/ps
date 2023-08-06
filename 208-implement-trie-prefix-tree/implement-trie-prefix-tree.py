class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, word: str) -> None:
        temp = self._trie
        for c in word:
            temp[c] = temp.get(c, {})
            temp = temp[c]
        temp[True] = True

    def search(self, word: str) -> bool:
        temp = self._trie
        for c in word:
            if c not in temp:
                return False
            temp = temp[c]
        return temp.get(True, False)
        
    def startsWith(self, prefix: str) -> bool:
        temp = self._trie
        for c in prefix:
            if c not in temp:
                return False
            temp = temp[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)