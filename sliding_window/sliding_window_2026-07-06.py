# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the size of the string and m is the character set size.
#
# Approach:
# Use a sliding window to keep track of the current substring. Utilize a set to store characters currently in the window, and expand the right end of the window by iterating through the string. If a character repeats, contract the left end until the substring is valid again.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
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
