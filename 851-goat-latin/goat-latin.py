class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return " ".join(f"{word if word[0].lower() in set('aeiou') else (word[1:]+word[0])}ma{'a'*i}" for i, word in enumerate(sentence.split(" "), 1))

