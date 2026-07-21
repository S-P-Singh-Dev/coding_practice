# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table, Sorting
# Time: O(N * K log K) where N is the number of strings and K is the maximum length of a string. | Space: O(N * K) for storing the anagrams in the dictionary.
#
# Approach:
# Sort each string to group anagrams together. Use a dictionary to map sorted strings to their original forms. Iterate through each string, sort it, and append it to the corresponding list in the dictionary. Finally, return the values as the result.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    return list(anagrams.values())
