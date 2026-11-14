# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(N * K * log(K)) where N is the number of words and K is the maximum length of a word. | Space: O(N * K) for storing the output in the hash table.
#
# Approach:
# Use a hash table (dictionary) to group words by their sorted tuple of characters. For each word, sort the characters and use it as a key. Append the word to the list corresponding to that key.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
