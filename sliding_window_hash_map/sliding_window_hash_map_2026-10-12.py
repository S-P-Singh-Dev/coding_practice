# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Map
# Time: O(n) | Space: O(min(n, m)) where n is the length of the input string and m is the character set size.
#
# Approach:
# Use a sliding window approach to maintain the longest substring without repeating characters. Utilize a hash map to track the last index of each character. Expand the window by moving the right pointer and contract from the left when a duplicate is found.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index_map:
            left = max(left, char_index_map[char] + 1)
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
