# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hash Table, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set
#
# Approach:
# Use a sliding window to keep track of the last seen indices of characters. Expand the window by adding characters from the right, and if a character repeats, shrink the window from the left until all characters are unique.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = max_length = 0
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
