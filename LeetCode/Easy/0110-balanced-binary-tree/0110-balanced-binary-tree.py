# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        y = [True]

        def walk(node):
            if not node:
                return 0

            left = walk(node.left)
            right = walk(node.right)
        
            if abs(left - right) > 1:
                y[0] = False

            return max(left, right) + 1

        walk(root)
        return y[0]
        