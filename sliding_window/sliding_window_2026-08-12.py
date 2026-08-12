# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# Use a sliding window to store characters and their indices. Expand the window by moving the right pointer and check for duplicates using a hash map. If a duplicate is found, move the left pointer to the right of the last occurrence of the duplicate character.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
