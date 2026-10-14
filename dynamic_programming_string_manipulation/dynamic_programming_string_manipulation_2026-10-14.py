# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming, String Manipulation
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Use a center expansion technique where we check for palindromes centered at each character and between each pair of characters. Expand outwards until the substring is no longer a palindrome.
#
# Solution:

def longest_palindrome(s: str) -> str:
    if not s or len(s) < 1:
        return ""
    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)  # odd length
        len2 = expand_around_center(s, i, i + 1)  # even length
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end + 1]


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
