# Add Two Numbers
# Difficulty: Medium
# Topic: Linked List, Mathematics
# Time: O(max(m, n)) where m and n are the lengths of the two linked lists. | Space: O(max(m, n)) for the new linked list.
#
# Approach:
# Use a dummy node to build the resulting linked list by summing each corresponding node of the two input lists. Keep track of the carry for sums exceeding 9.
#
# Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
