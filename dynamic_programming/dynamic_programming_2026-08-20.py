# Regular Expression Matching
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(m * n) | Space: O(m * n)
#
# Approach:
# Use a 2D DP table where dp[i][j] is True if s[0...i-1] matches p[0...j-1]. Initialize dp[0][0]. Iterate through s and p, handling '*' and '.' accordingly for transitions.
#
# Solution:

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    return dp[m][n]
