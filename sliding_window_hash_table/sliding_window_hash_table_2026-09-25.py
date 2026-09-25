# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window technique to maintain a substring without repeating characters. Use a hash map to store the last seen index of each character. Expand the window to the right and update the left pointer when a repeat is found.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
