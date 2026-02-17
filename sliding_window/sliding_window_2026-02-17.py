# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where m is the size of the character set
#
# Approach:
# Use two pointers to create a sliding window that can expand and contract. Maintain a set to track the characters currently in the window. If a repeating character is found, move the left pointer to reduce the window until the character can be added again.
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
