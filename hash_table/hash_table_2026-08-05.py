# String Permutation Check
# Difficulty: Medium
# Topic: Hash Table
# Time: O(n + m) where n and m are the lengths of the two strings. | Space: O(1) since the character set is constant.
#
# Approach:
# Use a character frequency count to compare the two strings. Count occurrences of each character in both strings, and then check if both counts match.
#
# Solution:

def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    count = [0] * 128  # assuming ASCII characters
    for char in s1:
        count[ord(char)] += 1
    for char in s2:
        count[ord(char)] -= 1
        if count[ord(char)] < 0:
            return False
    return True
