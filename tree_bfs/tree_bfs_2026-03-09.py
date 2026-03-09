# Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: Tree, BFS
# Time: O(n), where n is the number of nodes in the tree. | Space: O(n), for storing the result.
#
# Approach:
# Use BFS to traverse the tree level by level. Add each level's nodes' values into a list and then append this list to the result.
#
# Solution:

from collections import deque

def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
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
