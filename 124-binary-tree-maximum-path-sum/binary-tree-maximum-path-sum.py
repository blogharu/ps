# 7:24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = root.val
        nodes = []
        temp = [root]
        while temp:
            nodes.append(temp)
            next_temp = []
            for node in temp:
                if node.left:
                    next_temp.append(node.left)
                if node.right:
                    next_temp.append(node.right)
            temp = next_temp
        while nodes:
            node = nodes.pop()
            for n in node:
                max_val = n.val
                if n.left:
                    max_val += n.left.mx
                if n.right:
                    max_val += n.right.mx
                answer = max(answer, max_val)
                n.mx = 0
                if n.left and n.left.mx > 0:
                    n.mx = max(n.mx, n.left.mx)
                if n.right and n.right.mx > 0:
                    n.mx = max(n.mx, n.right.mx)
                n.mx = max(0, n.mx + n.val)
        return answer
        