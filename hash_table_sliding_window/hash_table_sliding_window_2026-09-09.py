# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hash Table, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of s and m is the character set size.
#
# Approach:
# Utilize a sliding window approach with a hash map to track the last seen index of each character. Expand the window by moving the right index and contract it from the left when a repeating character is found. Keep updating the maximum length of substrings without repeating characters.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
