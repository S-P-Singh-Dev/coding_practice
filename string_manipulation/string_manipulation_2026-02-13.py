# Longest Palindromic Substring
# Difficulty: Medium
# Topic: String Manipulation
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Expand around the center for each character and between each pair of characters to find and track the longest palindromic substring.
#
# Solution:

def longest_palindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(i, i)
        longest = max(longest, odd_palindrome, key=len)
        # Even length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, even_palindrome, key=len)
    return longest
