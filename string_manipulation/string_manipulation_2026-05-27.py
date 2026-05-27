# Longest Palindromic Substring
# Difficulty: Medium
# Topic: String Manipulation
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Use expand-around-center technique to check for palindromes. Iterate through the string and expand around each character (and between characters) to find the longest palindromic substring.
#
# Solution:

def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end + 1]

def expandAroundCenter(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
