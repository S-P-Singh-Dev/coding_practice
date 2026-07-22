# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the charset
#
# Approach:
# Use a sliding window with two pointers to track the longest substring without repeating characters. Expand the right pointer to include new characters and contract the left pointer if a character is repeated, updating the maximum length accordingly.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
