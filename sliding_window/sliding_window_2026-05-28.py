# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where m is the size of the character set.
#
# Approach:
# Use a sliding window to keep track of characters and their indexes. Increment the right pointer to expand the window and adjust the left pointer when a repeating character is found to maintain the substring's uniqueness.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left, max_length = 0, 0

    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
