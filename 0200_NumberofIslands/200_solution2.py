import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        direction = [(1, 0),
                     (-1, 0),
                     (0, 1),
                     (0, -1)]
        
        lands = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    lands.add((i, j))
        
        res = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in lands:
                    lands.remove((i, j))
                    queue = collections.deque([(i, j)])
                    while queue:
                        row, col = queue.popleft()
                        for d in direction:
                            r, c = row + d[0], col + d[1]
                            if (r, c) in lands:
                                lands.remove((r, c))
                                queue.append((r, c))
                    res += 1
                    
        return res
        

