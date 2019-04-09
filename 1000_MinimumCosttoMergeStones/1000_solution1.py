class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        
        dp = [[[float("Inf") for _ in range(K+1)] for _ in range(n+1)] for _ in range(n)]
        # dp[i][j][k]: cost of merging stones[i:j] into k piles
        # dp size: n * (n + 1) * (K + 1)
        # return dp[0][n][1]
        
        # initialize 
        for i in range(n):
            dp[i][i+1][1] = 0
            
        # l: sub-problem length, l = j - i
        for l in range(2, n+1):
            for i in range(n - l + 1):
                j = i + l
                for k in range(2, K + 1):
                    for m in range(i+1, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m][j][k-1])
                if dp[i][j][K] < float("Inf"):
                    dp[i][j][1] = dp[i][j][K] + sum(stones[i:j])
                    
        return dp[0][n][1]
