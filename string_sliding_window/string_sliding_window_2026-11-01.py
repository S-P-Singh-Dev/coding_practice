# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: String & Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window to expand and contract the substring while tracking characters in a hash map. If a duplicate character is found, shrink the window from the left until no duplicates remain.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = max_length = 0
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length
