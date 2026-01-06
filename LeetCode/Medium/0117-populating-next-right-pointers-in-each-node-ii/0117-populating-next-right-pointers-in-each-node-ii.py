"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)

        while queue and root:
            n = len(queue)
            
            for i in range(len(queue)):
                node = queue.popleft()

                if queue and i < n-1:
                    node.next = queue[0]
                else:
                    node.next = None

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return root