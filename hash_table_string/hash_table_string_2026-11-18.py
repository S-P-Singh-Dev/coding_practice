# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table, String
# Time: O(n * k log k), where n is the number of words and k is the maximum length of a word. | Space: O(n * k), for storing the grouped anagrams.
#
# Approach:
# To group anagrams, we can use a hash table where the key is a sorted version of the word. For each word, sort the characters and use the sorted string as the key to a list of words in the anagram group.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
