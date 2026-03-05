# Maximal Square
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(n) - We can optimize to use just one row.
#
# Approach:
# Maintain a DP array where dp[i][j] indicates the size of the largest square whose bottom-right corner is at (i, j). For each cell with '1', update the value as the minimum of the three neighbors (above, left, and top-left diagonal) plus one. Track the maximum size during the process.
#
# Solution:

def maximalSquare(matrix):
    if not matrix:
        return 0
    max_side = 0
    n = len(matrix[0])
    dp = [0] * (n + 1)
    prev = 0
    for i in range(1, len(matrix) + 1):
        for j in range(1, n + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == '1':
                dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return max_side * max_side
