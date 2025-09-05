#https://leetcode.com/problems/sort-matrix-by-diagonals/
# Difficulty:Hard
# Time:o(nlogn)
# 
# # Space:O(N)
# Python
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        R = len(grid)         # number of rows
        C = len(grid[0])      # number of columns

        S = collections.defaultdict(list)   # dictionary: key = diagonal ID, value = list of elements

        # Step 1: Group numbers by diagonals
        for x in range(R):
            for y in range(C):
                S[x - y].append(grid[x][y])
        
        # Step 2: Sort each diagonal’s elements
        for k in S.keys():
            S[k] = collections.deque(sorted(S[k]))
        
        # Step 3: Place back into grid in the right order
        for x in range(R):
            for y in range(C):
                if x - y >= 0:   # diagonals starting from top-left to bottom
                    grid[x][y] = S[x - y].pop()
                else:            # diagonals starting from bottom-left to top
                    grid[x][y] = S[x - y].popleft()

        return grid