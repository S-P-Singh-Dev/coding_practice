# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the size of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window technique with two pointers to iterate through the string while maintaining the longest substring without repeating characters using a set to track seen characters.
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
