# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window technique to expand the window until a repeating character is found, while maintaining the last seen index of characters to adjust the start of the window. Move the end pointer to explore characters and the start pointer to skip duplicates.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index_map:
            start = max(start, char_index_map[s[end]] + 1)
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length
