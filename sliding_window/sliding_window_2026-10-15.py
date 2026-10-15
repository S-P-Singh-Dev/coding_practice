# Find All Anagrams in a String
# Difficulty: Medium
# Topic: Sliding Window
# Time: O(n) | Space: O(1)
#
# Approach:
# Utilize a sliding window to keep track of character counts in the current substring and compare it with the character counts of the target anagram.
#
# Solution:

def find_anagrams(s, p):
    from collections import Counter
    p_count = Counter(p)
    s_count = Counter()
    result = []
    p_length = len(p)

    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= p_length:
            if s_count[s[i - p_length]] == 1:
                del s_count[s[i - p_length]]
            else:
                s_count[s[i - p_length]] -= 1
        if s_count == p_count:
            result.append(i - p_length + 1)

    return result
