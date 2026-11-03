# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use the sliding window technique with a hash map to store character indices. Expand the right end of the window while checking for duplicates. If a duplicate is found, move the left end of the window to the right of the last occurrence of the duplicate character.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index_map:
            left = max(left, char_index_map[char] + 1)
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
