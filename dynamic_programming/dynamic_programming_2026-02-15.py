# Unique Paths II
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(n)
#
# Approach:
# Use a 2D DP array to track the number of unique paths to each cell, initializing based on obstacles. Update paths based on the cells above and to the left.
#
# Solution:

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
    return dp[-1]
