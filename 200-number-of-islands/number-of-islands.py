class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0

        def dfs(r,c):
            if 0 > r or r >= len(grid) or 0 > c or c >= len(grid[0]) or grid[r][c] != '1':
                return
            else:
                grid[r][c] = '0'
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    total += 1
                    dfs(r,c)
        return total
