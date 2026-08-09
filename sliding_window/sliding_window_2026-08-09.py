# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m))
#
# Approach:
# Use a sliding window to track the characters in the current substring while utilizing a hash set to check for duplicates. Expand the right end of the window by moving one character at a time, and adjust the left end of the window whenever a duplicate is found.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        longest = max(longest, right - left + 1)

    return longest
