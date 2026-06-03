# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n^2) | Space: O(n^2)
#
# Approach:
# Use a dynamic programming table to track substrings. For each character, check if the current substring is a palindrome by validating adjacent characters and the previously computed values in the table.
#
# Solution:

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_length = i, 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_length = i, length
    return s[start:start + max_length]
