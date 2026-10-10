# Word Search II
# Difficulty: Medium
# Topic: Backtracking, Trie
# Time: O(M * N * 4^L) where M is the number of rows, N is the number of columns of the board, and L is the maximum length of a word. | Space: O(K + L) where K is the number of words in the Trie and L is the maximum length of a word.
#
# Approach:
# Use a Trie to store the words and a DFS to search through the board. For each cell, recursively explore all 4 directions if the current cell matches a prefix of any word. Mark cells as visited to avoid reuse and backtrack accordingly.
#
# Solution:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board, words):
        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node, path):
            if node.is_end_of_word:
                result.add(path)
                node.is_end_of_word = False  # Avoid duplicates
            if not (0 <= r < rows) or not (0 <= c < cols):
                return
            temp = board[r][c]
            node = node.children.get(temp)
            if not node:
                return
            board[r][c] = '#'  # Mark as visited
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(r + dr, c + dc, node, path + temp)
            board[r][c] = temp  # Restore cell

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, '')
        return list(result)
