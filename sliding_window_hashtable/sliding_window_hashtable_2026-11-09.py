# Find All Anagrams in a String
# Difficulty: Medium
# Topic: Sliding Window, HashTable
# Time: O(n) | Space: O(1)
#
# Approach:
# Use a sliding window to create a frequency count of characters in the substring of the target string that matches the length of the anagram. Compare this frequency count with the frequency count of the anagram. If they match, record the starting index.
#
# Solution:

def find_anagrams(s: str, p: str) -> List[int]:
    from collections import Counter
    p_count = Counter(p)
    s_count = Counter(s[:len(p)-1])
    results = []
    for i in range(len(p)-1, len(s)):
        s_count[s[i]] += 1  # include a new char in the window
        if s_count == p_count:
            results.append(i - len(p) + 1)
        s_count[s[i - len(p) + 1]] -= 1  # remove the oldest char from the window
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]
    return results
