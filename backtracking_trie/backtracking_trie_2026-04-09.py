# Word Search II
# Difficulty: Medium
# Topic: Backtracking, Trie
# Time: O(N * M * L) where N is the number of rows, M is the number of columns, and L is the length of the longest word. | Space: O(K) where K is the total number of characters in all words (for the Trie).
#
# Approach:
# Utilize a Trie data structure to efficiently store and search for words in a grid. Perform Depth-First Search (DFS) from each cell to find words by exploring adjacent cells.
#
# Solution:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        found = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def backtrack(x, y, node, path):
            char = board[x][y]
            node = node.children[char]
            if node.is_word:
                found.add(path)
                node.is_word = False  # Avoid duplicate entries
            board[x][y] = '#'  
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] in node.children:
                    backtrack(nx, ny, node, path + board[nx][ny])
            board[x][y] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    backtrack(i, j, trie.root, board[i][j])
        return list(found)
