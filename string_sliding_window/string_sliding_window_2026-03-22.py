# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: String, Sliding Window
# Time: O(n) | Space: O(min(n, m)), where n is the length of the string and m is the charset size (e.g., 26 for lowercase letters).
#
# Approach:
# Use a sliding window approach to maintain a substring without repeating characters. Utilize a hash set to track characters in the current window and adjust the starting position when a duplicate is found.
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
