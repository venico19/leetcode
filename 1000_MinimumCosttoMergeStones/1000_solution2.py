class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        
        dp = [[float("Inf") for _ in range(n+1)] for _ in range(n)]
        # dp[i][j]: mininal cost of merging stones[i:j] into minimal piles
        # minimal piles number: (j-i-1)%(K-1) + 1
        
        # dp size: n * (n + 1)
        # return dp[0][n]
        
        # initialize 
        for i in range(n):
            dp[i][i+1] = 0
            
        # l: sub-problem length, l = j - i
        for l in range(2, n+1):
            for i in range(n - l + 1):
                j = i + l
                m = i + 1
                while m < j:
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m][j])
                    m += (K-1)
                if (j-i-1)%(K-1) == 0:
                    # merge K piles to 1 if possible
                    dp[i][j] += sum(stones[i:j])
                    
        return dp[0][n]
