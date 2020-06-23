# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    prev_visited = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.prev_visited and root.val <= self.prev_visited:
            return False

        self.prev_visited = root.val

        if not self.isValidBST(root.right):
            return False
        return True
