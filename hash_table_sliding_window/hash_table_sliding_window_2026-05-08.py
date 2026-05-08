# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hash Table, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window and a hash map to keep track of characters and their indices. Expand the window by adding new characters until a duplicate is found, then shrink from the left until the substring is valid again.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = max_length = 0
    for right in range(len(s)):
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
