# Word Search II
# Difficulty: Medium
# Topic: Backtracking, Trie
# Time: O(M * N * L), where M is the number of rows, N is the number of columns in the board and L is the length of the longest word. | Space: O(K + W), where K is the size of the Trie and W is the number of words in the list.
#
# Approach:
# Build a Trie from the list of words and perform DFS for each cell in the board to find valid words. Use backtracking to explore all possible directions.
#
# Solution:

class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.is_end = False\n\ndef findWords(board, words):\n    def backtrack(x, y, node, word):\n        if len(word) >= 1 and node.is_end:\n            result.add(word)\n            node.is_end = False\n        if not (0 <= x < len(board) and 0 <= y < len(board[0])): return\n        temp = board[x][y]\n        node = node.children.get(temp)\n        if not node: return\n        board[x][y] = '#'\n        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):\n            backtrack(x + dx, y + dy, node, word + temp)\n        board[x][y] = temp\n\n    root = TrieNode()\n    for word in words:\n        node = root\n        for char in word:\n            if char not in node.children:\n                node.children[char] = TrieNode()\n            node = node.children[char]\n        node.is_end = True\n    result = set()\n    for i in range(len(board)):\n        for j in range(len(board[0])):\n            backtrack(i, j, root, '')\n    return list(result)
