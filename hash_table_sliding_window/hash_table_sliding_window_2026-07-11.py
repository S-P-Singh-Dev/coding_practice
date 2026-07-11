# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hash Table, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window approach with a hash table to track characters and their indices. Expand the window by moving the right pointer, and if a character repeats, move the left pointer to the right of the last occurrence.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
