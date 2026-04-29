# Add Two Numbers
# Difficulty: Medium
# Topic: Linked List
# Time: O(max(m, n)) where m and n are the lengths of the two linked lists. | Space: O(1) for list pointers; O(max(m, n)) for the resultant linked list, which is necessary.
#
# Approach:
# Simulate the addition process by traversing both linked lists and adding corresponding digits, managing carryover when the sum exceeds 9.
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
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
