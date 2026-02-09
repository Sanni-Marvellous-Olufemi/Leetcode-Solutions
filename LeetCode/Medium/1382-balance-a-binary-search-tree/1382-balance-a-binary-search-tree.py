# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = []

        def check(node):
            if not node:
                return
            
            check(node.left)
            tree.append(node.val)
            check(node.right)

        def walk(start, end):
            if start > end:
                return 

            mid = (start + end) // 2
            node = TreeNode(tree[mid])
            node.left = walk(start, mid - 1)
            node.right = walk(mid + 1, end)
            return node

        check(root)
        return walk(0, len(tree)-1)