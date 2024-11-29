class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m = len(grid)
        n = len(grid[0])

        # dfs to flip 1 to 0
        def dfs(grid, row, col) -> None:
            grid[row][col] = "0"
            for dir in dirs:
                newRow, newCol = row + dir[0], col + dir[1]
                if (0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == "1"):
                    dfs(grid, newRow, newCol)
        
        # traverse the grid to find the number of island
        for row in range(m):
            for col in range(n):
                if (grid[row][col] == "1"):
                    print('row, col', row, col)
                    dfs(grid, row, col)
                    res += 1

        return res