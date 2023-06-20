# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def depth_Tree(self, root):
        if root is None:
            return 0

        return max(self.depth_Tree(root.left), self.depth_Tree(root.right)) + 1

    def minDepth_Tree(self, root, max_depth):
        if root is None:
            return max_depth
        if root.left is None and root.right is None:
            return 1

        return min(self.minDepth_Tree(root.left, max_depth), self.minDepth_Tree(root.right, max_depth)) + 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.depth_Tree(root)
        return self.minDepth_Tree(root, depth)


