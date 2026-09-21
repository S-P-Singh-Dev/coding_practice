# Group Anagrams
# Difficulty: Medium
# Topic: Hashing
# Time: O(n * k log k) where n is the number of words and k is the maximum length of a word. | Space: O(n * k) for storing the groups of anagrams.
#
# Approach:
# Use a dictionary to group words with the same character frequency. Sort each word and use the sorted word as a key to aggregate anagrams into lists.
#
# Solution:

def groupAnagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
