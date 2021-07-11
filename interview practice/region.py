#
# # Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# # A region is captured by flipping all 'O's into 'X's in that surrounded region.
#

# X 0 X X X
# X O O X X
# X X O X X
# O O X O X
# X O X X X

# X X X X X
# X E E X X
# X X E X X
# X O X E X
# X X E E X

# X X X X X
# X X X X X
# X X X X X
# X X X O X
# X X O O X

# https://leetcode.com/problems/surrounded-regions/

import collections

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])
        for i in range(n):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
            if board[m - 1][i] == 'O':
                self.dfs(board, m - 1, i)
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][n - 1] == 'O':
                self.dfs(board, i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, row, col):
        visited = set()
        queue = collections.deque([(row, col)])
        visited.add((row, col))
        while queue:
            row, col = queue.popleft()
            board[row][col] = 'E'
            for delta_x, delta_y in DIRECTIONS:
                next_row = row + delta_x
                next_col = col + delta_y

                if self.is_valid(board, next_row, next_col, visited):
                    queue.append((next_row, next_col))
                    visited.add((next_row, next_col))

    def is_valid(self, board, x, y, visited):
        n, m = len(board), len(board[0])
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if (x, y) in visited:
            return False
        if board[x][y] == 'O':
            return True

        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """