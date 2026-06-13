# Binary Tree Right Side View
# Difficulty: Medium
# Topic: Tree, Depth-First Search, Breadth-First Search
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a level-order traversal (BFS) to access nodes level by level. At each level, the last node added to the result list will be visible from the right side.
#
# Solution:

from collections import deque

def rightSideView(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if i == level_length - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
