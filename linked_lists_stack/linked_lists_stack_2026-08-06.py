# Add Two Numbers II
# Difficulty: Medium
# Topic: Linked Lists, Stack
# Time: O(n + m) | Space: O(n + m)
#
# Approach:
# Use two stacks to reverse the linked lists and then add the numbers digit by digit from the least significant to the most significant.
#
# Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while stack1 or stack2 or carry:
            sum = carry
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            carry = sum // 10
            node = ListNode(sum % 10)
            node.next = head
            head = node

        return head
