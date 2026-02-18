# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Two Pointers, Hash Table
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# Use a sliding window technique with two pointers to track the start and end of the current substring. Use a hash map to store the last index of each character. If a character is repeated, move the start pointer to the right of the last occurrence of that character.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length
