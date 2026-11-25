# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the string length and m is the character set size.
#
# Approach:
# Use a sliding window technique with a hash map to track the last index of each character. Expand the window by moving the right pointer to include new characters and use the left pointer to discard the first repeating character.
#
# Solution:

def length_of_longest_substring(s):
    char_index_map = {}
    left = max_length = 0
    for right, char in enumerate(s):
        if char in char_index_map:
            left = max(left, char_index_map[char] + 1)
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
