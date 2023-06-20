# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = deque([root])

        while q:
            level = []

            for _ in range(0, len(q)):

                cur = q.popleft()

                level.append(cur.val if cur else "#")

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

            if len(level) > 1:
                n = len(level)
                fh, sh = level[:n // 2], level[n // 2:][::-1]
                if fh != sh:
                    return False
        return True