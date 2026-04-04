# Longest Repeating Character Replacement
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(1)
#
# Approach:
# Use a sliding window to track the count of characters in the current substring. Maintain a maximum frequency of a character and ensure the length of the window minus the maximum frequency does not exceed the allowed character replacements.
#
# Solution:

def characterReplacement(s: str, k: int) -> int:
    count = [0] * 26
    left = 0
    max_count = 0
    for right in range(len(s)):
        count[ord(s[right]) - ord('A')] += 1
        max_count = max(max_count, count[ord(s[right]) - ord('A')])
        while (right - left + 1) - max_count > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1
    return len(s) - left
