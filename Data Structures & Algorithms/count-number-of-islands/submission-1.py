class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[1,0], [0,-1], [-1,0], [0,1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        nb_inslands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr,dc in directions:
                    dfs(r+ dr, c+ dc)
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    nb_inslands += 1

        return nb_inslands

        