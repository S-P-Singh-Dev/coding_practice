# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the size of the character set.
#
# Approach:
# Use a sliding window to track the longest substring. Maintain a set of characters in the current window. Expand the window by moving the right pointer and check if the character is in the set. If it is, move the left pointer to shrink the window until the character can be added. Update the maximum length found.
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
