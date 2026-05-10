# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Expand around the center to check for palindromes. For each index, consider both single-character and two-character centers. Update a global longest palindrome length and result string whenever a longer palindrome is found.
#
# Solution:

def longestPalindrome(s):
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end + 1]


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
