# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, curr):
            if not node:
                return [True, curr]

            y, curr = check(node.left, curr)

            if curr >= node.val or not y:
                return [False, node.val]

            y, curr = check(node.right, node.val)
            return [y, max(node.val, curr)]

        return check(root, -float("inf"))[0]