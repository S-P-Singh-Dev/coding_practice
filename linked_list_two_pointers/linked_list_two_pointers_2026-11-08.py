# Swapping Nodes in a Linked List
# Difficulty: Medium
# Topic: Linked List, Two Pointers
# Time: O(N), where N is the number of nodes in the linked list. | Space: O(1), as we are using a constant amount of extra space.
#
# Approach:
# Use two pointers to find the nth node from the beginning and the nth node from the end. Then swap their values without altering the structure of the list.
#
# Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head
        # Move first to the k-th node
        for _ in range(k - 1):
            first = first.next
        # Move last to the k-th node from the end
        temp = first
        while temp.next:
            last = last.next
            temp = temp.next
        # Swap values
        first.val, last.val = last.val, first.val
        return head
