# Path Sum II
# Difficulty: Medium
# Topic: Tree, DFS
# Time: O(N), where N is the number of nodes in the tree. | Space: O(H), where H is the height of the tree, due to the recursion stack.
#
# Approach:
# Use Depth-First Search to explore all paths from the root to leaf nodes. Maintain a running sum and a path list. When reaching a leaf node, check if the running sum equals the target sum, if so, record the path.
#
# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, current_path, current_sum):
            if not node:
                return
            current_path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right and current_sum == targetSum:
                res.append(list(current_path))
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            current_path.pop()
            
        dfs(root, [], 0)
        return res
