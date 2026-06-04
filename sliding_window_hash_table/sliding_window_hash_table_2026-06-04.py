# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(n) | Space: O(min(n, m)), where n is the length of the string and m is the character set size
#
# Approach:
# Utilize a sliding window approach with two pointers to track the beginning and end of the substring. Use a hash set to store characters currently in the substring. Expand the right pointer, and if a duplicate character is found, move the left pointer until the substring becomes valid again.
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
