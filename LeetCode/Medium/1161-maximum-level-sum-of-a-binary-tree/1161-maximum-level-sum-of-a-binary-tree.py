# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        sums, level = -float("inf"), 0

        while queue:
            curr = 0
            for i in range(len(queue)):
                node = queue.popleft()
                curr += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            level += 1
            if curr > sums:
                sums = curr
                ans = level

        return ans
        