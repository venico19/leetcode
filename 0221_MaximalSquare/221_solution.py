class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        # dp[i][j]: size of max square including grid[i][j]
        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            res = max(res, dp[0][j])
            
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            res = max(res, dp[i][0])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if dp[i - 1][j] > 0 and dp[i][j - 1] > 0:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                        res = max(res, dp[i][j] ** 2)

        return res
            
