# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of words and K is the maximum length of a word. | Space: O(NK), for storing the grouped anagrams.
#
# Approach:
# Use a hash table to group words that are anagrams of each other. Sort each word and use the sorted word as a key to append original words in a list. Finally, return the grouped anagrams.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
