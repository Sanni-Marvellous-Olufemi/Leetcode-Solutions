# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr, y = -float("inf"), True

        def check(node):
            nonlocal curr, y
            if y:
                if not node:
                    return y

                check(node.left)
                
                if curr >= node.val:
                    y = False
                    return False
                
                curr = node.val
                check(node.right)

            return y

        return check(root)