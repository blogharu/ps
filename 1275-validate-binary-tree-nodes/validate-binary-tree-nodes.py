class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodes = [{'val': i} for i in range(n)]
        for i in range(n):
            if (li := leftChild[i]) != -1:
                if 0 in nodes[li] or nodes[i].get(0) == nodes[li]:
                    return False
                nodes[i][1] = nodes[li]
                nodes[li][0] = nodes[i]
            if (ri := rightChild[i]) != -1:
                if 0 in nodes[ri] or nodes[i].get(0) == nodes[ri]:
                    return False
                nodes[i][2] = nodes[ri]
                nodes[ri][0] = nodes[i]
        nodes = [node for node in nodes if node.get(0) == None]
        if len(nodes) != 1:
            return False
        count = 0
        done = set()
        while nodes:
            node = nodes.pop()
            if node['val'] in done:
                return False
            done.add(node['val'])
            if 1 in node:
                nodes.append(node[1])
            if 2 in node:
                nodes.append(node[2])
            count += 1
        if count != n:
            return False
        return True
