# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(min(n, m)) where n is the length of the input string and m is the size of the character set.
#
# Approach:
# Utilize a sliding window approach to maintain a window of unique characters. Use a hash set to track characters and expand the window until a duplicate is found, then contract from the left side until the substring is valid again.
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
