# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)), where n is the length of the input string and m is the character set size.
#
# Approach:
# Utilize a sliding window approach with two pointers and a hash set to track characters. Expand the window by moving the right pointer and contract by moving the left pointer when a repeat is found, keeping track of the maximum length of non-repeating characters.
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
