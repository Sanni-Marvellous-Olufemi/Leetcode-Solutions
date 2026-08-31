# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first, prev, count = float("inf"), -float("inf"), 1
        curr = head
        node = curr.next
        ans = [float("inf"), -float("inf")]

        while node.next:
            if (curr.val < node.val > node.next.val) or (curr.val > node.val < node.next.val):
                ans[0], ans[1] = min(ans[0], count - prev), max(ans[1], count-first)

                first = count if first == float("inf") else first
                prev = count

            count += 1
            curr = node
            node = node.next

        return ans if ans != [float("inf"), -float("inf")] else [-1,-1]
