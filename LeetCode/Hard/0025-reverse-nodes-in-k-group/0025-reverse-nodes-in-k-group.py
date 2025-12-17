# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        fast = head
        curr = head
        dummy = None
        count, length = 0, 0
        queue = deque()

        while fast and fast.next:
            fast = fast.next.next
            length += 2
        
        if fast:
            length += 1

        while curr:
            if length % k == length - count:
                queue.append(curr)
                break

            next_node = curr.next
            curr.next = dummy
            dummy = curr
            curr = next_node
            count += 1

            if count % k == 0:
                queue.append(dummy)
                dummy = None

        node = queue.popleft()
        temp = node
        while node and queue:
            if not node.next:
                node.next = queue.popleft()
                
            node = node.next


        return temp
