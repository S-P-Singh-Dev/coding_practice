# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window with two pointers to track the start and end of the current substring. Use a hash set to store characters and check for duplicates as you expand the end pointer. Adjust the start pointer when a duplicate is found to maintain the uniqueness of the substring.
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
