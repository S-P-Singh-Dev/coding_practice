# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where m is the size of the character set.
#
# Approach:
# Use a sliding window technique to maintain a substring of unique characters. Expand the window by moving the end pointer and contract from the start pointer when a duplicate is found, while updating the maximum length.
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
