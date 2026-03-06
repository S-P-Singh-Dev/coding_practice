# Longest Palindromic Substring
# Difficulty: Medium
# Topic: String Manipulation
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Use the expand around center technique to find all possible palindromes by iterating through each character and treating it as the center of a potential palindrome. Expand outwards as long as the characters match.
#
# Solution:

def longest_palindrome(s: str) -> str:
    if not s or len(s) < 1:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expand_around_center(s, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
