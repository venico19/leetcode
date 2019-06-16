class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        # dp[i][j]: continous width on ith row, ending with matrix[i][j]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + 1
                width = dp[i][j]
            
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    if width == 0:
                        break
                    area = width * (i-k+1)
                    res = max(res, area)
                    
        return res
        