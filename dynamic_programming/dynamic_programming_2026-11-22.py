# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n^2) | Space: O(n^2)
#
# Approach:
# Use dynamic programming to maintain a table that tracks whether substrings are palindromes. Iterate through each character, expanding around each character and between pairs of characters to detect palindromes.
#
# Solution:

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    table = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    for i in range(n):
        table[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and table[i + 1][j - 1]:
                table[i][j] = True
                start = i
                max_length = length
    return s[start:start + max_length]
