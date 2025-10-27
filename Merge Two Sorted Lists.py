# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()   # Dummy head node
        tail = dummy         # Pointer to build the merged list
        
        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move tail forward
        
        # Attach the remaining nodes
        tail.next = list1 if list1 else list2
        
        # Return merged list (skip dummy node)
        return dummy.next
