# Group Anagrams
# Difficulty: Medium
# Topic: String
# Time: O(N * K log K) where N is the number of strings and K is the maximum length of a string. | Space: O(N * K) for storing the grouped anagrams.
#
# Approach:
# Sort each string in the list and use it as a key in a hashmap to group anagrams together.
#
# Solution:

def groupAnagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # sort the string and use it as a key
        anagrams[key].append(s)
    return list(anagrams.values())
