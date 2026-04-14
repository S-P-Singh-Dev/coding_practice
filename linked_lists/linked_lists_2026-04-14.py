# Add Two Numbers
# Difficulty: Medium
# Topic: Linked Lists
# Time: O(max(m, n)) where m and n are the lengths of the two linked lists. | Space: O(max(m, n)) for the resulting linked list.
#
# Approach:
# Create a dummy node to help build the resulting linked list. Iterate through both linked lists, summing corresponding digits along with any carry from the previous digit. Create new nodes as needed and track the carry until all digits are processed.
#
# Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
