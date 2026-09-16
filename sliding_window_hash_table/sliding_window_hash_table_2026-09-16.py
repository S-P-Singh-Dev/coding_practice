# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m))
#
# Approach:
# Use a sliding window technique where we maintain a window of characters, expanding it until we encounter a repeating character. Utilize a hash table to track the last index of characters. If we find a repeat, we move the start of the window to the right of the last occurrence.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    longest = 0
    start = 0
    for index, char in enumerate(s):
        if char in char_index:
            start = max(start, char_index[char] + 1)
        char_index[char] = index
        longest = max(longest, index - start + 1)
    return longest
