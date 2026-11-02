# Number of Islands
# Difficulty: Medium
# Topic: Depth-First Search (DFS)
# Time: O(M*N), where M is the number of rows and N is the number of columns. | Space: O(M*N) in the worst case for the recursion stack.
#
# Approach:
# Traverse the grid and use DFS to explore each island. Mark cells as visited by changing '1' to '0'. Count each island encountered.
#
# Solution:

def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # mark as visited
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
