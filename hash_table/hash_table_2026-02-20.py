# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of strings and K is the maximum length of a string. | Space: O(NK), for storing the results in the hash map.
#
# Approach:
# Sort each string to define the key for grouping. Use a hash map to collect anagrams together based on the sorted key.
#
# Solution:

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
