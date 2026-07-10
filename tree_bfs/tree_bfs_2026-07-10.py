# Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: Tree, BFS
# Time: O(n), where n is the number of nodes in the tree, as each node is visited once. | Space: O(w), where w is the maximum width of the tree, which can occur at the last level.
#
# Approach:
# Use a queue to perform a breadth-first search (BFS) on the binary tree. Start by enqueuing the root node, then repeatedly dequeue nodes to access their values, enqueuing their children until all levels are processed.
#
# Solution:

from collections import deque

def levelOrder(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
