# Binary Tree Maximum Path Sum
# Difficulty: Medium
# Topic: Tree
# Time: O(n) | Space: O(h)
#
# Approach:
# Use Depth-First Search (DFS) to traverse the binary tree and calculate the maximum path sum at each node. Maintain a global variable to track the maximum sum found. For each node, consider paths that include the node itself and extend to its left and right children.
#
# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
