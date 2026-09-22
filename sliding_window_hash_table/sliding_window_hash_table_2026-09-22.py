# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m)) where n is the size of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window technique with a hash table to track the last occurrence of characters. Expand the right end of the window and contract the left as needed to ensure all characters are unique.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
