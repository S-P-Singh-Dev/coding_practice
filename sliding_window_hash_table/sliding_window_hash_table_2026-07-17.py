# Minimum Window Substring
# Difficulty: Medium
# Topic: Sliding Window, Hash Table
# Time: O(N + M), where N is the length of the string and M is the length of the target. | Space: O(M), for the hash table storing the character counts.
#
# Approach:
# Use a two-pointer technique to create a sliding window that expands and contracts based on whether the current window contains all characters of the target string. Maintain frequency counts of characters using a hash table.
#
# Solution:

from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    dict_t = Counter(t)
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    min_length = float('inf')
    min_left = 0

    while right < len(s):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while left <= right and formed == required:
            character = s[left]
            if right - left + 1 < min_length:
                min_left = left
                min_length = right - left + 1

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            left += 1
        right += 1
    return "" if min_length == float('inf') else s[min_left:min_left + min_length]
