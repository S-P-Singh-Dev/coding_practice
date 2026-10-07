# Group Anagrams
# Difficulty: Medium
# Topic: Sorting, Hashing
# Time: O(NK log K) where N is the number of strings and K is the maximum length of a string. | Space: O(NK) for storing the results in the hash map.
#
# Approach:
# Use a hash map to group words that are anagrams by their sorted character sequence.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    return list(anagrams.values())
