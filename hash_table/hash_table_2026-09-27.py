# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of words and K is the maximum length of a word. | Space: O(NK), for storing the anagrams in groups.
#
# Approach:
# Sort each word to create a unique key that represents its anagram group. Use a dictionary to map these keys to a list of words that belong to that group. Finally, return the values from the dictionary.
#
# Solution:

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
