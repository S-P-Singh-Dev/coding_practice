# Find All Anagrams in a String
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(N * M) | Space: O(1)
#
# Approach:
# Utilize a sliding window approach with character counts to identify anagrams of a target string within a given string. Maintain two frequency counts—one for the target and one for the current window—and compare them.
#
# Solution:

from collections import Counter

def find_anagrams(s: str, p: str):
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    result = []

    if p_count == s_count:
        result.append(0)

    for i in range(len(p), len(s)):
        s_count[s[i]] += 1
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]
        if p_count == s_count:
            result.append(i - len(p) + 1)

    return result
