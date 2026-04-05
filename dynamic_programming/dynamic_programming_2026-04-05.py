# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Use the expand around center approach to check for palindromes. For each character, expand outwards and track the longest palindrome found.
#
# Solution:

def longest_palindrome(s: str) -> str:
    if len(s) < 1:
        return ""

    start, end = 0, 0

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if (right - left - 1) > (end - start):
            start = left + 1
            end = right - 1

    for i in range(len(s)):
        expand_around_center(i, i)   # Odd length
        expand_around_center(i, i + 1)  # Even length

    return s[start:end + 1]
