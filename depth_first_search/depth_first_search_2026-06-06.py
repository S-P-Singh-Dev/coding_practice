# Word Search
# Difficulty: Medium
# Topic: Depth-First Search
# Time: O(M * N * 4^L) | Space: O(L)
#
# Approach:
# Utilize Depth-First Search (DFS) to explore each cell in the grid. For each cell, check if it matches the first letter of the word, then recursively check its neighbors. Maintain a visited set to avoid revisiting cells. If all characters are found consecutively, return True.
#
# Solution:

def exist(board, word):
    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = '#'  # mark as visited
        found = (dfs(i + 1, j, k + 1) or
                  dfs(i - 1, j, k + 1) or
                  dfs(i, j + 1, k + 1) or
                  dfs(i, j - 1, k + 1))
        board[i][j] = temp  # unmark
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
