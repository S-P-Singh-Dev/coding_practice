# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where m is the character set size
#
# Approach:
# Use a sliding window to maintain a substring without repeating characters. Expand the window by moving the right pointer and check for repeats using a hash set. If a repeat is found, move the left pointer to reduce the window until the repeat is eliminated.
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
