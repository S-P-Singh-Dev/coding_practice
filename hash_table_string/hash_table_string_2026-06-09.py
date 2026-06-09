# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table, String
# Time: O(NK log K), where N is the number of strings and K is the maximum length of a string. | Space: O(NK) for the hash table storing the grouped anagrams.
#
# Approach:
# Use a hash table to group the words by their sorted tuple of characters as the key. Iterate through the words, sort each word, and append it to the corresponding list in the hash table. Finally, return the values of the hash table.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
