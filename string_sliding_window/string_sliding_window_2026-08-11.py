# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: String, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# Utilize a sliding window technique with a hash map to store the indices of characters. Expand the window by moving the right pointer and, when a character repeats, move the left pointer to exclude the repeating character until all characters in the window are unique.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left, max_length = 0, 0
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
