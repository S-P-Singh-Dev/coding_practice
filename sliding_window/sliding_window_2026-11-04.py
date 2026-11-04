# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window approach with two pointers to maintain a current substring without duplicates. A hashmap can track the last index of each character to efficiently adjust the start of the window.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)
        char_index_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
