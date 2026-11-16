# Group Anagrams
# Difficulty: Medium
# Topic: Hash Table, String
# Time: O(NK log K), where N is the number of strings and K is the maximum length of a string. | Space: O(NK), the space used for the output and the hash table.
#
# Approach:
# To group anagrams, sort each string and use it as a key in a dictionary. Append all strings that match the same sorted key to a list. Finally, return the values of the dictionary as the grouped anagrams.
#
# Solution:

def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())
