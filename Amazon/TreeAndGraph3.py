# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        inorder_tree = []

        def inOrder(root: TreeNode):
            if root is None:
                return
            inOrder(root.left)
            inorder_tree.append(root.val)
            inOrder(root.right)

        inOrder(root)
        min_diff = abs(target - inorder_tree[0])
        closest_number = inorder_tree[0]
        for num in inorder_tree:
            diff = abs(target - num)
            if diff < min_diff:
                min_diff = diff
                closest_number = num
        return closest_number


a = TreeNode(6)
b = TreeNode(34)
c = TreeNode(0)
d = TreeNode(12)
d.left = a
d.right = b
a.left = c
print(Solution().closestValue(d, 3.45))
