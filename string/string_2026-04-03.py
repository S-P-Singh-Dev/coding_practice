# Group Anagrams
# Difficulty: Medium
# Topic: String
# Time: O(n * k log k), where n is the number of strings and k is the maximum length of a string. | Space: O(n * k), for storing the grouped anagrams.
#
# Approach:
# Use a hashmap to group words by their sorted character tuple. Iterate through each word, sort it, and use the sorted tuple as a key to group anagrams together.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        sorted_str = tuple(sorted(s))
        anagrams[sorted_str].append(s)
    return list(anagrams.values())
