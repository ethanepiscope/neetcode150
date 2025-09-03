# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(n) time, O(n) space due to recursion stack. Depth first traversal

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            right = root.right
            root.right = root.left
            root.left = right
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root

        