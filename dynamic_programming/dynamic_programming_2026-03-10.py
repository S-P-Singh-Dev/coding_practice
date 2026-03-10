# Distinct Subsequences
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(n)
#
# Approach:
# Use a 2D DP table where dp[i][j] represents the number of distinct subsequences of S[:i] that equal T[:j]. If the characters match, add both the previous counts and the count without the current character. Otherwise, carry forward the count without the current character.
#
# Solution:

def numDistinct(S: str, T: str) -> int:
    m, n = len(S), len(T)
    if n == 0:
        return 1
    if m == 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(n + 1):
        dp[0][j] = 0
    dp[0][0] = 1

    for i in range(1, m + 1):
        dp[i][0] = 1
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]
