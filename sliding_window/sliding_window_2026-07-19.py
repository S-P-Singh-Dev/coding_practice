# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)), where n is the length of the string and m is the charset size.
#
# Approach:
# Use a sliding window to keep track of the longest substring without repeating characters. Use a set to check for duplicates while expanding the window. When a duplicate is found, shrink the window from the left until the duplicate is removed.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
