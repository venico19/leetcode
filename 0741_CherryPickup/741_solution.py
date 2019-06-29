class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0
        
        memo = {}
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 >= N or c1 >= N or r2 >= N or c2 >= N or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float("Inf")
            
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]
            
            if r1 == N - 1 and c1 == N - 1:
                ans = grid[N-1][N-1]
            else:
                ans = grid[r1][c1] + (r1 != r2) * grid[r2][c2]
                ans += max(
                    dp(r1 + 1, c1, r2),
                    dp(r1 + 1, c1, r2 + 1),
                    dp(r1, c1 + 1, r2),
                    dp(r1, c1 + 1, r2 + 1)
                )
            memo[(r1, c1, r2)] = ans
            return ans
        
        return max(0, dp(0, 0, 0))