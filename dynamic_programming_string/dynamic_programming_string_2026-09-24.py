# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming, String
# Time: O(n^2) | Space: O(n^2)
#
# Approach:
# Use a dynamic programming array to record substrings that are palindromic. For each substring, check if the characters at both ends match and validate the substring in between. This allows building longer palindromes based on shorter ones.
#
# Solution:

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and length > max_length:
                    max_length = length
                    start = i
    return s[start:start + max_length]
