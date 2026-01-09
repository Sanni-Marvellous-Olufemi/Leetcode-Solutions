# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels, ans, count, y = 0, None, 0, False

        def check(node, level):
            nonlocal levels, count, ans

            if not node:
                return
            
            if not node.left and not node.right:
                if level == levels:
                    count += 1
                    ans = node
                elif level > levels:
                    count = 1
                    levels = level
                    ans = node

            check(node.left, level+1)
            check(node.right, level+1)
        
        check(root, 0)
        if count == 1:
            return ans


        def walk(node, level):
            nonlocal levels, ans, count, y

            if not node:
                return 0

            if level == levels:
                return 1

            curr = walk(node.left, level+1) + walk(node.right, level+1)

            if curr == count and not y:
                ans = node
                y = True
            
            return curr

        walk(root, 0)
        return ans

                