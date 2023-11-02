# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def update_answer(node):
            n, s = 1, node.val
            for child in [node.left, node.right]:
                if child is not None:
                    update_answer(child)
                    n += child.n
                    s += child.s
            if node.val == s // n:
                self.answer += 1
            node.n = n
            node.s = s                    
        update_answer(root)
        return self.answer