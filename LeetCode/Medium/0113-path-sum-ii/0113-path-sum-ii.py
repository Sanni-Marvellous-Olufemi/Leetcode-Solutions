# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def walk(node, path):
            if not node:
                return

            path.append(node.val)

            ans.append(path[:]) if (not node.right and not node.left) and (sum(path)== targetSum) else 0

            walk(node.left, path)
            walk(node.right, path)
            path.pop()

        walk(root, [])
        return ans
            

            