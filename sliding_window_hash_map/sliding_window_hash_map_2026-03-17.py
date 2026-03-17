# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Map
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Use a sliding window technique to expand the substring until a repeating character is found. Keep track of the characters' indices in a hash map. If a repeat is found, move the left pointer of the window. Update the maximum length accordingly.
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
