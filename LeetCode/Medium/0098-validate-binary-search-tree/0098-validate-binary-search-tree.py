# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = -float("inf")

        def check(node):
            nonlocal curr

            if not node:
                return True

            check(node.left)

            if curr >= node.val:
                return False
            
            curr = node.val
            return check(node.right)

        return check(root)