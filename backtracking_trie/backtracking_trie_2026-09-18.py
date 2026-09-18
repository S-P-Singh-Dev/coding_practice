# Word Search II
# Difficulty: Medium
# Topic: Backtracking, Trie
# Time: O(N * M * L), where N is the number of rows, M is the number of columns, and L is the length of the longest word. | Space: O(W + N * M), where W is the number of words stored in the Trie.
#
# Approach:
# Utilize a Trie data structure to store the words for efficient lookup. Implement backtracking to search for words on the board. For each starting cell, explore all possible paths in the 4 cardinal directions, marking cells as visited to avoid revisits.
#
# Solution:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, node, path):
        if node.is_end:
            result.add(path)
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        char = board[r][c]
        if char not in node.children:
            return
        next_node = node.children[char]
        board[r][c] = '#'  # mark as visited
        
        backtrack(r + 1, c, next_node, path + char)
        backtrack(r - 1, c, next_node, path + char)
        backtrack(r, c + 1, next_node, path + char)
        backtrack(r, c - 1, next_node, path + char)
        board[r][c] = char  # unmark

    for r in range(rows):
        for c in range(cols):
            backtrack(r, c, trie.root, '')

    return list(result)
