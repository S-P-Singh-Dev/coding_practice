# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window to maintain the current substring without repeating characters. Use a hash map to track characters and their indices. Increase the start of the window as needed to ensure there are no duplicates, and keep track of the maximum length found.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    max_length = 0
    start = 0
    for index, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = index
        max_length = max(max_length, index - start + 1)
    return max_length
