# Group Anagrams
# Difficulty: Medium
# Topic: String
# Time: O(NK log K) where N is the number of words and K is the maximum length of a word. | Space: O(NK) for storing the result in the hashmap.
#
# Approach:
# Use a hashmap to group words that are anagrams by their sorted character tuple as a key. Iterate through the list of words, sort each word, and append it to the corresponding list in the hashmap.
#
# Solution:

def groupAnagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[tuple(sorted(word))].append(word)
    return list(anagrams.values())
