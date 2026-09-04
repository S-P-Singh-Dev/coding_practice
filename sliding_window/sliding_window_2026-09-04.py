# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window technique with two pointers to track the start and end of the current substring. Use a set to keep track of the characters in the substring. Expand the window by moving the end pointer; if a duplicate character is found, move the start pointer until the duplicate is removed.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    chars_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in chars_set:
            chars_set.remove(s[left])
            left += 1
        chars_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
