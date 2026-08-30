# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m)) where n is the size of the string and m is the character set size.
#
# Approach:
# Use a sliding window to keep track of characters in the current substring. Move the right pointer to extend the substring and use a set to check for duplicates. If a duplicate is found, move the left pointer to shrink the window until the substring is valid again.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
