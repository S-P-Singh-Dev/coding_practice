# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: String
# Time: O(n) | Space: O(min(n, m)) where n is the length of the input string and m is the character set size.
#
# Approach:
# Use a sliding window with two pointers to keep track of the beginning and end of the substring. Use a set to store the characters in the current substring. If a character is repeated, move the start pointer until the substring is valid again.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
