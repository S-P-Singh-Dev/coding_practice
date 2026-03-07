# Count Unique Characters of All Substrings of a Given String
# Difficulty: Medium
# Topic: String, HashMap
# Time: O(n) | Space: O(1)
#
# Approach:
# For each character in the string, calculate its contribution to unique character counts in all substrings ending at that position. Use two pointers to track the last occurrence of each character and a cumulative count of unique characters.
#
# Solution:

def uniqueCharCount(s: str) -> int:
    last_index = {}  
    unique_count = 0  
    total_count = 0  

    for i, char in enumerate(s):  
        unique_count = (i - last_index.get(char, -1))  
        total_count += unique_count  
        last_index[char] = i  

    return total_count
