# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# Use a sliding window technique with two pointers to maintain a substring without repeating characters. Use a hash map to track the last index of each character.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
