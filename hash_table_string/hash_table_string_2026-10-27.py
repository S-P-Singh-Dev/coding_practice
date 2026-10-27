# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table, String
# Time: O(N K log K), where N is the number of strings and K is the maximum length of a string. | Space: O(N K) to store the hash table.
#
# Approach:
# Use a hash table to group strings by their sorted tuple of characters. For each string, sort it and use the sorted string as a key in the hash table. Append the original string to the corresponding list in the hash table. Finally, return the values of the hash table.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
