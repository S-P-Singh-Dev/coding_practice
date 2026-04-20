# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Strings, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window approach with two pointers to expand the window until a repeating character is found. Use a hash map to track the indices of characters and their latest positions. Adjust the left pointer to exclude the repeating character and continue expanding.
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
