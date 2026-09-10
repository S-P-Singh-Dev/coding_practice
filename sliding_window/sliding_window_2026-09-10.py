# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use two pointers to create a dynamic window that tracks the longest substring without repeating characters. Expand the window by moving the right pointer, and when a duplicate is found, contract the left pointer until the substring is valid again.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = max_length = 0
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
