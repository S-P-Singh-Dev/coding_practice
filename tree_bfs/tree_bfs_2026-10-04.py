# Binary Tree Level Order Traversal II
# Difficulty: Medium
# Topic: Tree, BFS
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a queue to perform a breadth-first search (BFS) on the tree, storing each level's node values. Traverse the tree level-by-level, appending values to a list. Finally, reverse the list of level values to get the order from bottom to top.
#
# Solution:

from collections import deque

def levelOrderBottom(root):
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
    return result[::-1]
