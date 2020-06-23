# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSame(root, root)

    def isSame(self, root1: TreeNode, root2: TreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return self.isSame(root1.left, root2.right) and self.isSame(
                    root1.right, root2.left
                )

        return False


t = TreeNode(1)
print(Solution().isSymmetric(t))
