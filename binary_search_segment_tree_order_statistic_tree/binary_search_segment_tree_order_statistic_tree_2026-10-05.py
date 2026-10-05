# Count Of Smaller Numbers After Self
# Difficulty: Medium
# Topic: Binary Search, Segment Tree, Order Statistic Tree
# Time: O(n log n) | Space: O(n)
#
# Approach:
# Use a modified Binary Search Tree to count how many numbers are smaller than the currents as we traverse the list from right to left.
#
# Solution:

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.result = []

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            node.count += 1
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = BSTNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = BSTNode(value)

    def count_smaller(self, root, value):
        if root is None:
            return 0
        if value <= root.value:
            return self.count_smaller(root.left, value)
        else:
            return root.count + 1 + self.count_smaller(root.right, value)

class Solution:
    def countSmaller(self, nums):
        bst = BST()
        for num in reversed(nums):
            bst.insert(num)
            bst.result.append(bst.count_smaller(bst.root, num))
        return list(reversed(bst.result))
