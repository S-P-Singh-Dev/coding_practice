# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(m, n)) where m is the character set size and n is the string length
#
# Approach:
# Use a sliding window approach to maintain a substring of unique characters. Expand the right end of the window by moving the pointer while keeping track of characters in a hash map. If a character repeats, move the left pointer to reduce the size of the window until the substring is unique again.
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
