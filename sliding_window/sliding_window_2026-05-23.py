# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window technique with a hash map to track the last indices of characters. Expand the right boundary to include new characters and contract the left boundary when a repeat is found, ensuring only unique characters are in the current window.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
