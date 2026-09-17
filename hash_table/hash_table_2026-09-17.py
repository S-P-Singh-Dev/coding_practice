# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(N * K log K) where N is the number of words and K is the maximum length of a word. | Space: O(N * K) for storing the grouped anagrams in the dictionary.
#
# Approach:
# Use a dictionary to map sorted tuples of characters to a list of anagrams. For each word, sort the characters and use the sorted tuple as a key to group the anagrams together.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
