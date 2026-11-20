# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Hash Table, Sliding Window
# Time: O(n) | Space: O(min(n, m))
#
# Approach:
# Utilize a sliding window approach with two pointers to track the current substring and a hash table to store the last occurrence of each character. Expand the right pointer until a duplicate is found, then slide the left pointer to exclude the duplicate and continue.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left, max_length = 0, 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
