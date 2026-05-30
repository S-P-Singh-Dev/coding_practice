# Swap Nodes in Pairs
# Difficulty: Medium
# Topic: Linked List
# Time: O(n) | Space: O(1)
#
# Approach:
# Iterate through the linked list in pairs and swap the nodes. Adjust the pointers accordingly to maintain links to the rest of the list.
#
# Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dummy.next
