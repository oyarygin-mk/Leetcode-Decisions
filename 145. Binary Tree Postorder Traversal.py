# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                ans.append(node.val)

        helper(root)

        return ans