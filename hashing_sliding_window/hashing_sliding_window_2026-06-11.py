# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hashing, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window to track characters and their indices. Expand the window by moving the right pointer and update the left pointer when a duplicate character is found.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = max_length = 0
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
