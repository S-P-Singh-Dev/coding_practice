# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the size of the input string and m is the character set size.
#
# Approach:
# Use a sliding window approach to maintain the longest substring without repeating characters. Utilize a set to track characters in the current window and adjust the window's start position whenever a duplicate character is found.
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
