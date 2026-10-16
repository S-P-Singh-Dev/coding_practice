# Decode Ways
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n) | Space: O(n)
#
# Approach:
# Use dynamic programming to count the number of ways to decode the string. Create a DP array where `dp[i]` represents the number of ways to decode the substring up to index `i`. Initialize base cases and fill the array based on valid character ranges.
#
# Solution:

def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[n]
