# Maximal Square
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(n)
#
# Approach:
# Use a dynamic programming approach to track the size of the largest square that can be formed at each cell of the matrix. Iterate through each cell of the matrix; if it contains a '1', update the current cell's DP value by checking the minimum of three neighboring squares (left, top, and top-left diagonal) plus one.
#
# Solution:

def maximalSquare(matrix):
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * (cols + 1)
    max_side = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[j] = min(dp[j], dp[j - 1], dp[j]) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
    return max_side ** 2
