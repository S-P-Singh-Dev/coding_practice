# Longest Substring Without Repeating Characters
# Difficulty: medium
# Topic: Hash Table, Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# We will use a sliding window approach with two pointers to find the longest substring without repeating characters. We'll maintain a set to track characters in the current window and expand or shrink the window based on repeated characters.
#
# Solution:

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
