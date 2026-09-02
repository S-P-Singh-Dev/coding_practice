# Number of Islands
# Difficulty: Medium
# Topic: Depth-First Search
# Time: O(M * N) where M is the number of rows and N is the number of columns in the grid. | Space: O(M * N) for the recursion stack in the worst case.
#
# Approach:
# Use Depth-First Search (DFS) to traverse each island. For each unvisited '1', perform a DFS to mark all its connected '1's as visited. Count each DFS initiation as a new island.
#
# Solution:

def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count
