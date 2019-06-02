class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        res = 0
        
        lands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    lands.add((i, j))
        
        for i in range(m):
            for j in range(n):
                if (i, j) in lands:
                    lands.remove((i, j))
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        for (x_dir, y_dir) in directions:
                            if (x+x_dir, y+y_dir) in lands:
                                lands.remove((x+x_dir, y+y_dir))
                                stack.append((x+x_dir, y+y_dir))
                    res += 1
                    
        return res
                    
        
        
