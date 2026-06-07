# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        sets = set()

        for parent, child, left in descriptions:
            sets.add(child)

            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)

            if child not in hashmap:
                hashmap[child] = TreeNode(child)

            if left == 1:
                hashmap[parent].left = hashmap[child]
            else:
                hashmap[parent].right = hashmap[child]

        for i in hashmap:
            if i not in sets:
                return hashmap[i]