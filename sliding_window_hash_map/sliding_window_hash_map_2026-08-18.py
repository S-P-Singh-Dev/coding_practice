# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Map
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window to maintain the current substring and a hash map to store the last seen index of each character. Expand the right end of the window with each character and check if it is already in the current substring. If it is, move the left end of the window to the right of its last seen index. Update the maximum length found during the traversal.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = max_length = 0
    for right, char in enumerate(s):
        if char in char_index_map:
            left = max(left, char_index_map[char] + 1)
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
