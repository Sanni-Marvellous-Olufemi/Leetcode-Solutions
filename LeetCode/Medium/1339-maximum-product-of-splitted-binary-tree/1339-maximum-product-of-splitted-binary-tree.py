# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sum, self.ans = 0, 0

        def sum(node):
            if not node:
                return
            
            self.sum += node.val
            sum(node.left)
            sum(node.right)

        def walk(node):
            if not node:
                return 0

            val = walk(node.left) + walk(node.right) + node.val
            self.ans = max(self.ans, val * (self.sum - val))

            return val

        sum(root)
        walk(root)
        return self.ans
