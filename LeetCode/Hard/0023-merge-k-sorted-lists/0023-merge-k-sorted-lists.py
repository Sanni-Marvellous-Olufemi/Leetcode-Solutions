# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        if not lists:
            return None

        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        temp = ListNode()
        curr = temp
        if heap:
            while heap:
                curr.next = ListNode(heapq.heappop(heap))
                curr = curr.next

        return temp.next