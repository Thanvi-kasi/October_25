# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node to simplify the head manipulation
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        
        # Traverse the list in pairs
        while prev_node.next and prev_node.next.next:
            first_node = prev_node.next
            second_node = prev_node.next.next
            
            # Swap the nodes
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node.next = second_node
            
            # Move prev_node two steps ahead
            prev_node = first_node
        
        # Return the new head (dummy.next)
        return dummy.next
