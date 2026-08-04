# 2352 Equal Pairs, Hashmap

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = {}

        # Count each row
        for row in grid:
            row = tuple(row)
            rows[row] = rows.get(row, 0) + 1

        pairs = 0
        n = len(grid)

        # Check each column
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            pairs += rows.get(col, 0)

        return pairs
        
# Time Complexity O(n^2)