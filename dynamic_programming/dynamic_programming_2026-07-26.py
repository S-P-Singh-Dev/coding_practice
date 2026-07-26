# Maximal Square
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(n)
#
# Approach:
# We will use dynamic programming to keep track of the maximal square of 1's we can form at each position. If we encounter a '1' in the grid, the size of the square is determined by the minimum of the values from the top, left, and top-left diagonal positions, plus one. We will continuously update the maximum side length of the square found.
#
# Solution:

def maximalSquare(matrix):
    if not matrix:
        return 0
    max_side = 0
    n = len(matrix[0])
    dp = [0] * (n + 1)
    for i in range(1, len(matrix) + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == '1':
                dp[j] = min(dp[j], dp[j - 1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return max_side * max_side
