# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels, ans = 0, None

        def walk(node, level, parent):
            nonlocal levels, ans

            if not node:
                return

            if not node.right and not node.left:
                if level >= levels:
                    ans = parent if parent.right and parent.left else node
                    levels = level
                return

            walk(node.left, level+1, node)
            walk(node.right, level+1, node)

        walk(root, 0, root)
        return ans

                