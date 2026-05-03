# Substring with Concatenation of All Words
# Difficulty: Medium
# Topic: String, Hash Table, Sliding Window
# Time: O(n * m), where n is the length of the string and m is the total number of words multiplied by their length. | Space: O(m), where m is the number of unique words due to the hash map.
#
# Approach:
# Use a sliding window approach combined with a hash map to count occurrences of each word. Iterate through the string, maintaining a window of size equal to the total length of words, and check if all words in the list are present in the current window.
#
# Solution:

from collections import Counter

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []
    word_length = len(words[0])
    num_words = len(words)
    total_length = word_length * num_words
    word_count = Counter(words)
    indices = []

    for i in range(len(s) - total_length + 1):
        window = s[i:i + total_length]
        window_words = [window[j:j + word_length] for j in range(0, total_length, word_length)]
        if Counter(window_words) == word_count:
            indices.append(i)

    return indices
