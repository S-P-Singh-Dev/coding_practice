# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table
# Time: O(N * K log K), where N is the number of words and K is the maximum length of a word (for sorting). | Space: O(N * K) for storing the anagram groups.
#
# Approach:
# Use a hash table (dictionary) to group words that are anagrams by sorting them. The sorted word serves as a key, while the original words are stored in a list as values.
#
# Solution:

def groupAnagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
