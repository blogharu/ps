class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}

        for product in products:
            temp = trie
            for c in product:
                temp[c] = temp.get(c, {"heap": []})
                temp = temp[c]
                heap = temp["heap"]
                heap.append(product)
                heap.sort()
                if len(heap) > 3:
                    heap.pop()

        temp = trie
        answer = []
        for c in searchWord:
            if c in temp:
                temp = temp[c]
                answer.append(temp["heap"])
            else:
                temp = {}
                answer.append([])

        return answer
