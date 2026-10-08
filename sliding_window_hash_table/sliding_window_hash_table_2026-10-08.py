# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Maintain a sliding window using two pointers and a hash set to track characters. Expand the right pointer to include new characters, and move the left pointer to ensure all characters are unique.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
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
