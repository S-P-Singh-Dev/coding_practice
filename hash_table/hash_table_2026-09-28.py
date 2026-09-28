# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of strings and K is the maximum length of a string. | Space: O(NK), for storing the results.
#
# Approach:
# Use a hash table to group words by their sorted characters. Sort each word to form a key and store the words in a list under that key. Finally, return the grouped anagrams from the hash table.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
