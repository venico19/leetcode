class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k >= n / 2:
            res = 0
            for i in range(1, n):
                res += max(prices[i] - prices[i-1], 0)
            return res
        
        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        # dp[i][j]: maxprofit with i transactions on day j
        
        for i in range(1, k+1):
            local = [0 for _ in range(n)]
            # local[j]: maxprofit, must sell on day j
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                local[j] = max(
                    dp[i-1][j-1] + profit,
                    dp[i-1][j-1],
                    local[j-1] + profit
                )
                dp[i][j] = max(dp[i][j-1], local[j])
                       
        return dp[-1][-1]
                