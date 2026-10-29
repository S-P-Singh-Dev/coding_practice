# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window approach with two pointers and a hashmap to track characters' indices. Expand the window with the right pointer and contract from the left to maintain unique characters.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
