# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)), where n is the length of the string and m is the character set size.
#
# Approach:
# Use a set to keep track of the characters in the current substring. Expand the window by moving the right pointer. If a repeating character is found, shrink the window from the left until the substring is valid again. Update the maximum length at each step.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    chars = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
