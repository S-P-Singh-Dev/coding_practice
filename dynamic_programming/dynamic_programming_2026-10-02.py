# Unique Paths II
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m*n) | Space: O(m*n)
#
# Approach:
# We'll use a dynamic programming approach to calculate the number of unique paths to each cell in the grid, accounting for obstacles. We'll set up a 2D dp array where dp[i][j] represents the number of ways to reach cell (i, j) from the start cell (0, 0). Initialize the dp array, and build it iteratively while avoiding obstacles.
#
# Solution:

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[-1][-1]
