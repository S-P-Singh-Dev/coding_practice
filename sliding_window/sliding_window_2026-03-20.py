# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window technique with a hash map to track characters' positions. Expand the right end of the window by adding characters, and adjust the left end accordingly when duplicates are found.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = max_length = 0
    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
