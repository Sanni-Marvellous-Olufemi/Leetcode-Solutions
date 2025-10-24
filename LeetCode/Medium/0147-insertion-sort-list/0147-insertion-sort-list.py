# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-float('inf'))
        dummy.next = head
        
        prev_sorted = head
        curr_unsorted = head.next
        
        while curr_unsorted:
            if curr_unsorted.val >= prev_sorted.val:
                prev_sorted = curr_unsorted
                curr_unsorted = curr_unsorted.next
            else:
                prev_sorted.next = curr_unsorted.next              
                start = dummy
                while start.next and start.next.val < curr_unsorted.val:
                    start = start.next
                
                temp = start.next
                start.next = curr_unsorted
                curr_unsorted.next = temp

                curr_unsorted = prev_sorted.next
                
        return dummy.next