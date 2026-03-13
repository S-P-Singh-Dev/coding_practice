# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m))
#
# Approach:
# Use a sliding window technique to maintain a substring that contains no repeating characters. Expand the window by moving the end pointer to include new characters until a duplicate is found. When a duplicate character is encountered, move the start pointer to shrink the window until there are no duplicates.
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
