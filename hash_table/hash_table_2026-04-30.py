# First Unique Character in a String
# Difficulty: Medium
# Topic: Hash Table
# Time: O(n) | Space: O(1) (only 26 letters considered)
#
# Approach:
# Use a counter to track the frequency of each character, then iterate through the string a second time to find the first character that occurs only once.
#
# Solution:

from collections import Counter

def firstUniqChar(s: str) -> int:
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
