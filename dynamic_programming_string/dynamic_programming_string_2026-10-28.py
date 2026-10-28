# Longest Palindromic Substring
# Difficulty: Medium
# Topic: Dynamic Programming, String
# Time: O(n^2) | Space: O(1)
#
# Approach:
# Use expand around center technique to evaluate potential palindromic substrings at each character position. For each character, expand outward to check for odd and even-length palindromes.
#
# Solution:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
