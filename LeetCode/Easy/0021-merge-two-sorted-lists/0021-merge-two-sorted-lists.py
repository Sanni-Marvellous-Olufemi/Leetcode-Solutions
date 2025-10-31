# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        new_list = ListNode()
        current_node = new_list

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
                current_node = current_node.next

            else:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
                current_node = current_node.next

        while list1:
            current_node.next = ListNode(list1.val)
            current_node = current_node.next
            list1 = list1.next

        while list2:
            current_node.next = ListNode(list2.val)
            current_node = current_node.next
            list2 = list2.next
        
        new_list = new_list.next
        return new_list

