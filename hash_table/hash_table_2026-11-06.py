# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of words and K is the maximum length of a word | Space: O(NK)
#
# Approach:
# Use a hash map to group words that are anagrams of each other. The key will be the sorted form of each word, and the value will be a list of words that match that key.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
