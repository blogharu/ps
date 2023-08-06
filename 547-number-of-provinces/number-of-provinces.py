class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        answer = 0
        roots = {i for i in range(len(isConnected))}
        while roots:
            node = roots.pop()
            nodes = {node}
            while nodes:
                node = nodes.pop()
                for i, val in enumerate(isConnected[node]):
                    if val and i in roots:
                        roots.remove(i)
                        nodes.add(i)
            answer += 1
        return answer