# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, HashMap
# Time: O(n) | Space: O(min(n, m)) where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize a sliding window technique with a set to keep track of characters in the current substring. Expand the window by moving the right pointer and add characters to the set. If a duplicate is found, move the left pointer to shrink the window until there are no duplicates.
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
