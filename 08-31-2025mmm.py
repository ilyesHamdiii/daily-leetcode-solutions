#https://leetcode.com/problems/sudoku-solver/description/
# Time:O(9^N).
# 
# # Space:O(1)
# Python



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])

        available = []

        rows = [[False] * 9 for _ in range(R)]
        cols = [[False] * 9 for _ in range(C)]
        cells = [[False] * 9 for _ in range(9)]

        for x in range(R):
            for y in range(C):
                if board[x][y] == ".":
                    available.append((x, y))
                else:
                    c = int(board[x][y]) - 1
                    rows[x][c] = True
                    cols[y][c] = True

                    bigx, bigy = x // 3, y // 3
                    cells[bigx * 3 + bigy][c] = True

        found = False

        def go(index):
            if index == len(available):
                nonlocal found
                found = True
                return

            x, y = available[index]
            bigx, bigy = x // 3, y // 3
            bigc = bigx * 3 + bigy
            for c in range(9):
                if rows[x][c] or cols[y][c] or cells[bigc][c]:
                    continue
                    
                board[x][y] = str(c + 1)
                rows[x][c] = cols[y][c] = cells[bigc][c] = True

                go(index + 1)
                if found:
                    return

                rows[x][c] = cols[y][c] = cells[bigc][c] = False
                board[x][y] = "."


        go(0)

