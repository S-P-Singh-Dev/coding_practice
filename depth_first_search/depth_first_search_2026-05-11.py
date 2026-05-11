# Number of Islands
# Difficulty: Medium
# Topic: Depth-First Search
# Time: O(M * N), where M is the number of rows and N is the number of columns in the grid. | Space: O(M * N) in the worst case for the recursion stack.
#
# Approach:
# Use Depth-First Search (DFS) to explore and mark all connected '1's (land) while traversing through the grid. Each time a new unvisited '1' is found, increment the island count and explore all its connected lands.
#
# Solution:

def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark as visited
        dfs(i + 1, j)  # Down
        dfs(i - 1, j)  # Up
        dfs(i, j + 1)  # Right
        dfs(i, j - 1)  # Left

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
