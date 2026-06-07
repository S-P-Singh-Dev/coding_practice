# Find All Anagrams in a String
# Difficulty: Medium
# Topic: Sliding Window, Hash Map
# Time: O(n) | Space: O(1)
#
# Approach:
# Use a sliding window of length equal to the target string. Maintain a count of characters in both the window and the target string. When the counts match, record the starting index. Slide the window one character at a time and update counts accordingly.
#
# Solution:

def find_anagrams(s: str, p: str) -> List[int]:
    from collections import Counter
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    result = []

    if s_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        s_count[s[i]] += 1
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]
        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result
