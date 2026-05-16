# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(n * k log k), where n is the number of strings and k is the maximum length of a string. | Space: O(n * k), since we store all the strings in the result.
#
# Approach:
# 1. Create a dictionary to map each unique sorted tuple of characters to a list of anagrams. 2. Iterate through each string, sort it, and append the original string to the corresponding list in the dictionary. 3. Return the values of the dictionary as a list of lists.
#
# Solution:

from collections import defaultdict

def groupAnagrams strs:
    anagrams = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    return list(anagrams.values())
