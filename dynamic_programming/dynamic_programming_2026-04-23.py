# Decode Ways
# Difficulty: Medium
# Topic: Dynamic Programming
# Time: O(n) | Space: O(1)
#
# Approach:
# Use dynamic programming to track the number of ways to decode the string up to each index. If the current character is valid (1-9), it can contribute to the total ways from the previous index. If the two-character substring formed with the previous character is valid (10-26), it contributes to the ways from two indices back.
#
# Solution:

def numDecodings(s: str) -> int:
    if not s or s[0] == '0': return 0
    prev, curr = 1, 1
    for i in range(1, len(s)):
        temp = curr
        if s[i] == '0':
            if s[i-1] in '12':
                curr = prev
            else:
                return 0
        else:
            curr += prev
        if 10 <= int(s[i-1:i+1]) <= 26:
            curr += temp
        prev = temp
    return curr
