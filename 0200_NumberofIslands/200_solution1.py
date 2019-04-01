class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        direction = [(1, 0),
                     (-1, 0),
                     (0, 1),
                     (0, -1)]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for d in direction:
                    dfs(i + d[0], j + d[1])
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
                    
        return res
        

