# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def walk(node):
            if not node or not node.next:
                return node
            
            fast = slow = node
            
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            right = walk(slow.next)
            slow.next = None
            left = walk(node)
            
            new = ListNode()
            curr = new

            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            while left:
                curr.next = left
                left = left.next
                curr = curr.next

            while right:
                curr.next = right
                right = right.next
                curr = curr.next

            return new.next

        return walk(head)