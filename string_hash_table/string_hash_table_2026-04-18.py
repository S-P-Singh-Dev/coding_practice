# Substring with Concatenation of All Words
# Difficulty: Medium
# Topic: String, Hash Table
# Time: O(n * m), where n is the length of the input string and m is the total length of all words. | Space: O(m), to store the counts of words in the hash map.
#
# Approach:
# Use a sliding window and a hash map to track word count. Iterate through the string to find valid starting positions for concatenated substrings. Adjust the window based on matches.
#
# Solution:

def findSubstring(s: str, words: List[str]) -> List[int]:
    from collections import Counter
    if not s or not words:
        return []
    word_count = len(words)
    word_len = len(words[0])
    total_len = word_count * word_len
    result = []
    words_counter = Counter(words)

    for i in range(len(s) - total_len + 1):
        window = s[i:i+total_len]
        if Counter([window[j:j+word_len] for j in range(0, total_len, word_len)]) == words_counter:
            result.append(i)
    return result
