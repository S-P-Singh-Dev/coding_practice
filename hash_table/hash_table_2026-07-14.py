# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of strings and K is the maximum length of a string. | Space: O(N * K), for storing the output.
#
# Approach:
# Sort each string to use as a key in a dictionary to group anagrams. Iterate through the list of strings, sorting each and adding them to the corresponding list in the dictionary. Finally, return the values of the dictionary as the result.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
