# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(n * k log k), where n is the number of strings and k is the maximum length of a string. | Space: O(n * k), for storing the grouped anagrams in the dictionary.
#
# Approach:
# Use a dictionary to group strings by their sorted tuple representation. Each string is sorted, and the sorted version is used as a key in the dictionary where all anagrams are appended to a list.
#
# Solution:

def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())
