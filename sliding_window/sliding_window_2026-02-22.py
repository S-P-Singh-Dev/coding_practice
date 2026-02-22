# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the size of the input string and m is the character set size.
#
# Approach:
# Use a sliding window technique with two pointers to track the start and end of the substring. Utilize a dictionary to record the last seen index of characters. If a repeating character is found, shift the start pointer to the right of its last seen index.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_length = 0
    start = 0
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length
