class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] != 1:
                return 0
            
            res = 1
            grid[i][j] = 2
            for x, y in moves:
                res += dfs(i + x, j + y)
                
            return res
        
        def isConnected(i, j):
            if i == 0:
                return True
            for x, y in moves:
                if i + x < 0 or i + x >= m or j + y < 0 or j + y >= n:
                    continue
                if grid[i + x][j + y] == 2:
                    return True
            return False
        
        # for every hit, grid value -1 
        for i, j in hits:
            grid[i][j] -= 1
            
        # mark all connected grid as 2 after all hits
        for j in range(n):
            dfs(0, j)
            
        # reversly add the block of each hit back
        res = [0 for _ in range(len(hits))]
        for k in range(len(hits) - 1, -1, -1):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and isConnected(i, j):
                res[k] = dfs(i, j) - 1
                
        return res
            
            
            