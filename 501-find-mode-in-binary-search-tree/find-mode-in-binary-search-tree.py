# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        def dfs(node):
            counts[node.val] += 1
            if node.right:
                dfs(node.right)
            if node.left:
                dfs(node.left)
        dfs(root)
        answer = []
        max_count = -1
        for val, count in counts.items():
            if count == max_count:
                answer.append(val)
            elif count > max_count:
                answer = [val]
                max_count = count
        return answer




            