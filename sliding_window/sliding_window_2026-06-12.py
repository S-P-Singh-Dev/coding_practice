# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)), where n is the length of the string and m is the character set size.
#
# Approach:
# Utilize the sliding window technique with a hash set to store the characters of the current substring. Expand the right end of the window until a duplicate character is found, then shrink from the left until the duplicate is removed.
#
# Solution:

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
