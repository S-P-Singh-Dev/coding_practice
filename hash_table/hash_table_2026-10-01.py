# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(NK log K), where N is the number of strings and K is the maximum length of a string. | Space: O(NK) for storing the group of anagrams.
#
# Approach:
# Use a hash table to group words that are anagrams by sorting the characters of each word as the key.
#
# Solution:

def groupAnagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    return list(anagrams.values())
