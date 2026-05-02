# Word Ladder
# Difficulty: Medium
# Topic: Graph, BFS
# Time: O(N * 26^L), where N is the number of words and L is the length of each word. | Space: O(N)
#
# Approach:
# Utilize Breadth-First Search (BFS) to explore all possible transformations of the start word until the end word is reached. Use a set to store the word list for O(1) lookups. For each word, generate potential 1-letter transformations and check if they exist in the word list.
#
# Solution:

from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append((new_word, length + 1))
    return 0
