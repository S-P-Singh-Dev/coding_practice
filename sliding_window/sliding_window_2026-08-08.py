# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# Utilize the sliding window technique with a hash map to track characters and their positions. Expand the window by moving the right pointer and shrink it from the left when a duplicate character is found.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
