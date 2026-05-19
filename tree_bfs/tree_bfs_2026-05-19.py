# Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: Tree, BFS
# Time: O(n), where n is the number of nodes in the tree. | Space: O(n), for storing the queue and the result list.
#
# Approach:
# Use a queue to perform a level-order traversal. Start from the root, enqueue its left and right children. Continue until all levels are processed.
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
