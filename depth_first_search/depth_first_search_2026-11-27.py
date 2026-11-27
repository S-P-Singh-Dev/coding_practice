# Number of Islands
# Difficulty: Medium
# Topic: Depth-First Search
# Time: O(m * n) | Space: O(min(m, n))
#
# Approach:
# Use Depth-First Search (DFS) to explore and mark all connected land cells ('1's) as visited. For each unvisited land cell, initiate a DFS which will traverse all adjacent land cells, effectively counting one island.
#
# Solution:

def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
