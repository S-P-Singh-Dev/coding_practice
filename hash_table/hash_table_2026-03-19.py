# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(n * k log k) where n is the number of strings and k is the maximum length of a string. | Space: O(n * k) for storing the hash table.
#
# Approach:
# Use a hash table to group words that are anagrams by sorting the characters of each word. The sorted word serves as the key in the hash table, and the values are lists of words that correspond to that key.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
