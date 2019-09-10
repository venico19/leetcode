class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        count = sum(grid[i][j]=='1' for i in range(m) for j in range(n))
        
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(i1, j1, i2, j2):
            nonlocal count
            p1 = find((i1, j1))
            p2 = find((i2, j2))
            if p1 != p2:
                parent[p1] = p2
                count -= 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                if j < n - 1 and grid[i][j+1] == '1':
                    union(i, j, i, j+1)
                if i < m - 1 and grid[i+1][j] == '1':
                    union(i, j, i+1, j)

        return count
                    