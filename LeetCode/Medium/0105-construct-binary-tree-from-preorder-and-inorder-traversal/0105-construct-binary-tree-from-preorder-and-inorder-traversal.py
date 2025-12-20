# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i, p, sets = 0, 0, set()

        def walk(curr):
            nonlocal i, p

            if i >= len(preorder) or p >= len(preorder):
                return

            sets.add(preorder[p])
            node = TreeNode(preorder[p])
            p += 1

            if preorder[curr] != inorder[i]:
                node.left = walk(p)

            if preorder[curr] == inorder[i]:
                i += 1
                if i < len(inorder) and inorder[i] not in sets:
                    node.right = walk(p)

            return node

        return walk(0)


            