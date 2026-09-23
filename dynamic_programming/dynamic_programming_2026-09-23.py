# Medium Number of Distinct Subsequences
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(n)
#
# Approach:
# Use a 2D DP array where dp[i][j] counts the number of distinct subsequences of the first i characters in 's' that form the first j characters of 't'. Initialize the first column for the empty target string and fill the table based on character matches or skips.
#
# Solution:

def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(n + 1):
        dp[0][j] = 0 if j > 0 else 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]
